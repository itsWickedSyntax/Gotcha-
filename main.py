#!/usr/bin/env python3
"""
Gotcha! - Advanced Username & Email OSINT Tool
A comprehensive reconnaissance tool for finding online profiles
"""

import argparse
import asyncio
import sys
import os
import warnings
from pathlib import Path

# Suppress aiohttp ResourceWarnings about unclosed sessions
warnings.filterwarnings("ignore", category=ResourceWarning, message="unclosed.*")
warnings.filterwarnings("ignore", category=ResourceWarning, message=".*client_session.*")
warnings.filterwarnings("ignore", category=ResourceWarning, message=".*connector.*")

# Add the modules directory to the path
sys.path.insert(0, str(Path(__file__).parent / "modules"))

from core.banner import print_banner
from core.logger import setup_logger
from core.config import Config
from engines.username_hunter import UsernameHunter
from engines.email_hunter import EmailHunter
from engines.social_media import SocialMediaHunter
from engines.breach_checker import BreachChecker
from utils.reporter import Reporter
from utils.validator import Validator

class Gotcha:
    def __init__(self):
        self.config = Config()
        self.logger = setup_logger()
        self.reporter = Reporter()
        
    async def run_username_scan(self, username, options):
        """Run comprehensive username reconnaissance"""
        self.logger.info(f"Starting username scan for: {username}")
        
        # Initialize hunters
        username_hunter = UsernameHunter()
        social_hunter = SocialMediaHunter()
        
        results = {
            'username': username,
            'social_media': [],
            'general_sites': [],
            'developer_platforms': [],
            'forums': [],
            'gaming': [],
            'adult_platforms': [],
            'misc': []
        }
        
        # Run scans
        if options.social:
            results['social_media'] = await social_hunter.hunt_username(username, include_adult=options.adult)
        
        if options.general:
            results['general_sites'] = await username_hunter.hunt_general_sites(username, include_adult=options.adult)
        
        if options.developer:
            results['developer_platforms'] = await username_hunter.hunt_developer_platforms(username)
        
        if options.forums:
            results['forums'] = await username_hunter.hunt_forums(username)
        
        if options.gaming:
            results['gaming'] = await username_hunter.hunt_gaming_platforms(username)
        
        if options.adult:
            results['adult_platforms'] = await username_hunter.hunt_adult_platforms(username)
        
        return results
    
    async def run_email_scan(self, email, options):
        """Run comprehensive email reconnaissance"""
        self.logger.info(f"Starting email scan for: {email}")
        
        # Validate email format
        if not Validator.is_valid_email(email):
            self.logger.error("Invalid email format")
            return None
        
        # Initialize hunters
        email_hunter = EmailHunter()
        breach_checker = BreachChecker()
        
        results = {
            'email': email,
            'breaches': [],
            'social_accounts': [],
            'professional_accounts': [],
            'domain_info': {}
        }
        
        try:
            # Run scans
            if options.breaches:
                results['breaches'] = await breach_checker.check_breaches(email)
            
            if options.social:
                results['social_accounts'] = await email_hunter.hunt_social_accounts(email)
            
            if options.professional:
                results['professional_accounts'] = await email_hunter.hunt_professional_accounts(email)
            
            if options.domain:
                results['domain_info'] = await email_hunter.analyze_domain(email)
        
        finally:
            # Ensure email hunter session is closed
            try:
                await email_hunter.close_session()
            except Exception as e:
                self.logger.warning(f"Error closing email hunter session: {str(e)}")
        
        return results

def main():
    parser = argparse.ArgumentParser(
        description="Gotcha! - Advanced Username & Email OSINT Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s -u john_doe --social --developer
  %(prog)s -e john@example.com --breaches --social
  %(prog)s -u username -e email@domain.com --all
  %(prog)s -u username --social --adult
  %(prog)s -f usernames.txt --output report.json
  
Note: Use --adult flag to include adult/NSFW platforms (18+ content)
        """
    )
    
    # Target options
    parser.add_argument('-u', '--username', help='Target username')
    parser.add_argument('-e', '--email', help='Target email address')
    parser.add_argument('-f', '--file', help='File containing usernames/emails (one per line)')
    
    # Scan options
    parser.add_argument('--social', action='store_true', help='Search social media platforms')
    parser.add_argument('--general', action='store_true', help='Search general websites')
    parser.add_argument('--developer', action='store_true', help='Search developer platforms')
    parser.add_argument('--forums', action='store_true', help='Search forums and communities')
    parser.add_argument('--gaming', action='store_true', help='Search gaming platforms')
    parser.add_argument('--breaches', action='store_true', help='Check for data breaches')
    parser.add_argument('--professional', action='store_true', help='Search professional networks')
    parser.add_argument('--domain', action='store_true', help='Analyze email domain')
    parser.add_argument('--adult', action='store_true', help='Search adult/NSFW platforms (18+ content)')
    parser.add_argument('--all', action='store_true', help='Enable all search modules')
    
    # Output options
    parser.add_argument('-o', '--output', help='Output file (JSON/CSV format)')
    parser.add_argument('--format', choices=['json', 'csv', 'txt'], default='json', help='Output format')
    parser.add_argument('--quiet', action='store_true', help='Suppress banner and verbose output')
    parser.add_argument('--threads', type=int, default=50, help='Number of concurrent threads')
    parser.add_argument('--timeout', type=int, default=10, help='Request timeout in seconds')
    
    args = parser.parse_args()
    
    # Validate that at least one target is specified
    if not any([args.username, args.email, args.file]):
        parser.error("At least one target must be specified: -u/--username, -e/--email, or -f/--file")
    
    # Print banner
    if not args.quiet:
        print_banner()
    
    # Set all options if --all is used
    if args.all:
        args.social = True
        args.general = True
        args.developer = True
        args.forums = True
        args.gaming = True
        args.breaches = True
        args.professional = True
        args.domain = True
        args.adult = True
    
    # Check if at least one scan option is selected
    scan_options = [args.social, args.general, args.developer, args.forums, 
                   args.gaming, args.breaches, args.professional, args.domain, args.adult]
    if not any(scan_options):
        parser.error("At least one scan option must be specified (or use --all)")
    
    # Initialize Gotcha
    gotcha = Gotcha()
    
    async def run_scan():
        results = []
        
        if args.file:
            # Process file
            try:
                with open(args.file, 'r') as f:
                    targets = [line.strip() for line in f if line.strip()]
                
                for target in targets:
                    if '@' in target:
                        result = await gotcha.run_email_scan(target, args)
                    else:
                        result = await gotcha.run_username_scan(target, args)
                    
                    if result:
                        results.append(result)
            except FileNotFoundError:
                print(f"Error: File '{args.file}' not found")
                return
        else:
            # Process single target(s)
            if args.username:
                result = await gotcha.run_username_scan(args.username, args)
                if result:
                    results.append(result)
            
            if args.email:
                result = await gotcha.run_email_scan(args.email, args)
                if result:
                    results.append(result)
        
        # Generate report
        if results:
            if args.output:
                gotcha.reporter.save_report(results, args.output, args.format)
            else:
                gotcha.reporter.print_report(results, args.quiet)
    
    # Run the async scan
    try:
        asyncio.run(run_scan())
    except KeyboardInterrupt:
        print("\n[!] Scan interrupted by user")
        sys.exit(1)

if __name__ == "__main__":
    main()
