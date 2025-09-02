# Contributing to Gotcha!

Thank you for your interest in contributing to Gotcha! This document provides guidelines and information for contributors.

## 🤝 Ways to Contribute

- **Bug Reports**: Report bugs or issues you encounter
- **Feature Requests**: Suggest new platforms or features
- **Code Contributions**: Submit pull requests with improvements
- **Documentation**: Improve documentation and examples
- **Platform Additions**: Add support for new platforms

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- Git
- Basic understanding of web scraping and OSINT techniques

### Setting Up Development Environment

1. **Fork the repository**
   ```bash
   git clone https://github.com/yourusername/gotcha.git
   cd gotcha
   ```

2. **Create a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a branch for your changes**
   ```bash
   git checkout -b feature/your-feature-name
   ```

## 📋 Submission Guidelines

### Pull Request Process

1. **Update the changelog** in `CHANGELOG.md`
2. **Test your changes** thoroughly
3. **Follow the coding standards** outlined below
4. **Write clear commit messages**
5. **Submit a pull request** with a detailed description

### Commit Message Format
```
type(scope): description

[optional body]

[optional footer]
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes
- `refactor`: Code refactoring
- `test`: Adding tests
- `chore`: Maintenance tasks

**Examples:**
```
feat(platforms): add support for Mastodon platform
fix(email): resolve Adobe account connection issue
docs(readme): update installation instructions
```

## 💻 Coding Standards

### Python Style Guide
- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and concise

### Code Structure
```python
async def check_platform_account(self, username: str) -> Optional[Dict[str, Any]]:
    """
    Check if username exists on platform
    
    Args:
        username: Target username to check
        
    Returns:
        Dictionary with account information or None if not found
    """
    try:
        # Implementation here
        pass
    except Exception as e:
        self.logger.error(f"Error checking {username}: {str(e)}")
        return None
```

### Adding New Platforms

When adding support for new platforms, follow this structure:

1. **Add platform configuration** to the appropriate hunter module
2. **Implement checking method** with proper error handling
3. **Add platform to filtering logic** if it's an adult platform
4. **Test the implementation** thoroughly
5. **Update documentation**

#### Example Platform Addition
```python
# In social_media.py or username_hunter.py
'newplatform': {
    'url': 'https://newplatform.com/{}',
    'check_url': 'https://newplatform.com/{}',
    'indicators': ['profile', 'user', 'account'],
    'not_found_indicators': ['not found', 'user not found']
}
```

## 🧪 Testing

### Manual Testing
- Test with various usernames and email addresses
- Verify error handling for non-existent accounts
- Check rate limiting and timeout behavior
- Test adult content filtering

### Test Cases to Cover
- Valid usernames/emails
- Invalid usernames/emails
- Special characters in usernames
- Network connectivity issues
- Platform-specific edge cases

## 📝 Platform Addition Guidelines

### Research Phase
1. **Analyze the platform**:
   - URL structure for profiles
   - Profile existence indicators
   - Anti-bot measures
   - Rate limiting policies

2. **Respect platform policies**:
   - Check robots.txt
   - Review Terms of Service
   - Implement appropriate delays

### Implementation Phase
1. **Add platform configuration**
2. **Implement checking logic**
3. **Handle errors gracefully**
4. **Add to appropriate category** (social, professional, etc.)
5. **Test thoroughly**

### Platform Categories
- **Social Media**: General social networking platforms
- **Professional**: Career and business-focused platforms
- **Developer**: Programming and development platforms
- **Gaming**: Gaming and entertainment platforms
- **Forums**: Discussion and community platforms
- **Adult**: 18+ content platforms (requires `--adult` flag)

## 🔒 Security Considerations

### Ethical Guidelines
- **Respect privacy**: Don't collect or store personal information
- **Follow laws**: Ensure compliance with local and international laws
- **Rate limiting**: Implement appropriate delays between requests
- **User consent**: Make adult content opt-in only

### Security Best Practices
- **Input validation**: Sanitize all user inputs
- **Error handling**: Don't expose sensitive information in errors
- **Logging**: Log actions but not personal data
- **Network security**: Use HTTPS and verify SSL certificates

## 📖 Documentation

### Code Documentation
- Add docstrings to all functions and classes
- Include parameter and return type information
- Provide usage examples where helpful

### User Documentation
- Update README.md for new features
- Add examples for new command-line options
- Update help text and usage information

## 🐛 Bug Reports

When submitting bug reports, please include:

- **Description**: Clear description of the issue
- **Reproduction steps**: How to reproduce the bug
- **Expected behavior**: What should happen
- **Actual behavior**: What actually happens
- **Environment**: OS, Python version, dependencies
- **Logs**: Relevant log output (sanitized)

## 💡 Feature Requests

For feature requests, please provide:

- **Use case**: Why this feature would be useful
- **Description**: Detailed description of the feature
- **Implementation ideas**: Suggestions for implementation
- **Alternatives**: Other solutions you've considered

## 📞 Getting Help

- **GitHub Issues**: For bugs and feature requests
- **Discussions**: For questions and general discussion
- **Security Issues**: Email privately for security vulnerabilities

## 🙏 Recognition

Contributors will be recognized in:
- CHANGELOG.md for their contributions
- README.md acknowledgments section
- Git commit history

## ⚖️ Code of Conduct

### Our Standards
- **Be respectful**: Treat all contributors with respect
- **Be inclusive**: Welcome diverse perspectives and backgrounds
- **Be constructive**: Provide helpful feedback and suggestions
- **Be ethical**: Use the tool responsibly and legally

### Unacceptable Behavior
- Harassment or discriminatory language
- Malicious use of the tool
- Sharing personal information without consent
- Violating platform terms of service

---

Thank you for contributing to Gotcha! Your efforts help make this tool better for the entire security research community.
