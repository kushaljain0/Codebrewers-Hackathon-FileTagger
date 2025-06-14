# Codebrewers-Hackathon-FileTagger

## Problem Statement

In today's digital world, managing and organizing files efficiently is a significant challenge. Users often struggle with:
- Manually categorizing and tagging large volumes of files
- Maintaining consistent file organization across different devices and platforms
- Finding specific files quickly when needed
- Understanding the content and context of files without opening them
- Managing file metadata and relationships between files

## Our Solution

FileTagger is an intelligent file management system that leverages artificial intelligence to automatically analyze, categorize, and tag files. Our solution addresses these challenges through:

### Key Features

1. **AI-Powered File Analysis**
   - Automatic content analysis using advanced AI models
   - Intelligent categorization based on file content and context
   - Smart tag generation for easy file discovery

2. **Smart Organization**
   - Automatic file categorization into logical groups
   - Custom tag creation and management
   - Intelligent file relationship mapping

3. **Efficient Search**
   - Advanced search capabilities using tags and categories
   - Content-based search functionality
   - Quick file discovery through smart filtering

4. **User-Friendly Interface**
   - Intuitive dashboard for file management
   - Easy-to-use tagging system
   - Visual representation of file relationships

### Technical Implementation

The system is built using modern web technologies and AI integration:
- Frontend: React-based user interface
- Backend: Python-based API server
- AI Integration: Advanced language models for content analysis
- Database: Efficient storage for file metadata and relationships

## Getting Started

### Prerequisites

- Python 3.x
- Windows OS (required for file system operations)
- Administrator privileges (for file system operations)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Codebrewers-Hackathon-FileTagger.git
   cd Codebrewers-Hackathon-FileTagger
   ```

2. Install required Python packages:
   ```bash
   pip install tkinter
   ```

3. Ensure you have the following files in your project directory:
   - `filetagger.py` - Main application file
   - `fileid-tags.json` - Stores file ID to tags mapping
   - `tag-fileids.json` - Stores tag to file IDs mapping

### Running the Application

1. Run the main application:
   ```bash
   python filetagger.py
   ```

2. The application will open with a graphical user interface where you can:
   - Add tags to files
   - Search files by tags
   - Remove tags from files
   - View all tags
   - Open tagged files

### Usage Guide

1. **Adding Tags**
   - Click "Add Tag" button
   - Select one or more files
   - Enter the tag name
   - Click "Add tag" to save

2. **Searching Files**
   - Click "Search Tag" button
   - Enter the tag name
   - View the list of files with that tag
   - Select a file to open or remove its tag

3. **Managing Tags**
   - Use "Remove Tags" to delete tags from files
   - Use "Show All Tags" to view all existing tags
   - Tags are automatically converted to lowercase and spaces are removed

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built for Codebrewers Hackathon
- Uses Windows File System utilities for file identification
- Implements a custom JSON-based tagging system
