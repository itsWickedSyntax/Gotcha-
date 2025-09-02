# **Gotcha! - Advanced Username & Email OSINT Tool**

Gotcha! is a powerful open-source OSINT tool designed to uncover online profiles and digital footprints associated with usernames and email addresses. It is built for security researchers, penetration testers, and digital investigators, offering comprehensive search capabilities across various platforms, including social media, adult, professional networks, and more.

# 💠 **Features**  
 
-	 Extensive Platform Coverage:
-	 Social Media: Twitter, Instagram, Facebook, LinkedIn, and more.
-	 Adult/NSFW: Pornhub, OnlyFans, Chaturbate, etc. (with opt-in filtering).
-	 Professional: GitHub, Stack Overflow, Professional Networks.
-	 Gamer, Developer, Forums, and many more!
-	 Email Breach Checks: Validate emails against known breach databases and conduct comprehensive searches for possible compromises.
-	 Mutually Exclusive Options: Flexibility to choose targeted platform categories like developer or adult platforms with specific flags.
-	 Modular Design: Easy to extend with custom platforms via configuration.
-	 Python Asyncio: Efficient, concurrent scanning using Python's asyncio for maximum performance.
-	 Connection Resilience: Built-in error handling to manage connection failures gracefully.


# ✨ **Installation & Usage**

1. Clone the Repo
2. install the requirements.txt file:
   
	 	pip3 install -r requirements.txt

   		cd gotcha
	
   	 	sudo python3 gotcha.py -h

--------------------------------------------------

# 🔞 **Adult Platform Support Added**

#### New Platforms Added:

#### Social Media Hunter (Adult Platforms):
- Video Platforms: Pornhub, XVideos, RedTube, Faphouse, ManyVids, Clips4Sale, iWantClips, JustForFans
- Cam Sites: Chaturbate, Cam4, MyFreeCams, StripChat, LiveJasmin, BongaCams, CamSoda
- Community: OnlyFans, FetLife

#### Username Hunter (Adult Platforms):
- Dating/Adult: AdultFriendFinder, Ashley Madison, Seeking, Alt.com, SwapperNet
- Content Creation: FapHouse, ManyVids, Clips4Sale, iWantClips, JustForFans

#### Email Hunter (Adult Platform Checks):
-	OnlyFans: Password reset API check
-	Pornhub: Registration page check
- 	Chaturbate: Password reset form check
- 	Cam4: Password reset check
- 	AdultFriendFinder: Password reset check

# New Features:

1. #### adult Command Line Flag: 
	-	Specifically enables adult/NSFW platform searches
	-	Separate from --all for user control
	-	Clear 18+ content warning in help text
2. #### Selective Filtering:
	-	Adult platforms are excluded by default
	-	Only included when --adult flag is used
	-	Maintains professional tool usage without explicit adult content
3. #### Proper Error Handling:
	-	Graceful handling of connection failures (common with adult sites)
	-	Warning-level logging instead of errors for unavailable sites
	-	Continues scanning other platforms when some fail
4. #### Enhanced Help Documentation:
	-	Clear examples showing adult option usage
	-	Warning about 18+ content
	-	Professional presentation

# Usage Examples:
#### Username search including adult platforms
	sudo python3 main.py -u username --social --adult

#### Email search including adult platforms  
	sudo python3 main.py -e email@domain.com --social --adult

#### Comprehensive scan including adult platforms
	sudo python3 main.py -u username -e email@domain.com --all

#### Adult platforms only
	sudo python3 main.py -u username --adult
   
# Security Research Benefits:

  -	Comprehensive OSINT: Now covers adult platforms for complete digital footprint analysis
  -	Privacy-Aware: Most adult sites protect user privacy, so results may be limited (which is expected)
  -	Professional Implementation: Clean separation between regular and adult content searches
  -	Ethical Usage: Clear labeling and opt-in approach for adult content

The tool now provides comprehensive coverage across all major online platforms while maintaining professional standards and giving users full control over the scope of their searches.

