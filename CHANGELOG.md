# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-07-04

### Added
- Initial release of Gotcha! OSINT Tool
- Username scanning across 50+ platforms
- Email address reconnaissance and verification
- Data breach checking capabilities
- Adult/NSFW platform support with opt-in flag
- Asynchronous scanning for improved performance
- Multiple output formats (JSON, CSV, TXT)
- Comprehensive error handling and logging
- Modular architecture for easy extension

### Features
- **Social Media Platforms**: Twitter, Instagram, Facebook, LinkedIn, YouTube, TikTok, Reddit, Pinterest, Snapchat, Discord, Twitch, Spotify, Medium, Behance, Dribbble, Vimeo, SoundCloud, Tumblr, Flickr
- **Developer Platforms**: GitHub, GitLab, Bitbucket, Stack Overflow, CodePen, Replit, HackerOne, Bugcrowd, Kaggle, Docker Hub, NPM, PyPI
- **Gaming Platforms**: Steam, Xbox, PlayStation, Epic Games, Battle.net, Minecraft, Roblox
- **Professional Networks**: LinkedIn, AngelList, Product Hunt
- **Forums & Communities**: Reddit, XDA Developers, Disqus, Discourse
- **Adult Platforms**: OnlyFans, Pornhub, Chaturbate, Cam4, MyFreeCams, StripChat, LiveJasmin, BongaCams, CamSoda, FetLife, AdultFriendFinder, Ashley Madison, Seeking
- **Email Services**: Gravatar, Microsoft Account, Adobe, Spotify password reset checks
- **Breach Databases**: Have I Been Pwned integration, local breach file support

### Technical Details
- Built with Python 3.8+ and asyncio for concurrent processing
- Uses aiohttp for efficient HTTP requests
- DNS resolution checking for improved reliability
- Configurable timeouts and rate limiting
- Comprehensive session management to prevent resource leaks
- Error handling with graceful degradation for blocked sites

### Command Line Interface
- Username targeting with `-u/--username`
- Email targeting with `-e/--email`
- Bulk processing with `-f/--file`
- Modular scan options: `--social`, `--developer`, `--gaming`, `--forums`, `--professional`, `--breaches`, `--domain`, `--adult`
- Output options: `--output`, `--format`, `--quiet`
- Performance tuning: `--threads`, `--timeout`

### Security & Privacy
- Ethical design with privacy considerations
- Adult content behind explicit opt-in flag
- No data storage or collection
- Respects platform rate limits and robots.txt where applicable
- Includes proper disclaimers for responsible use
