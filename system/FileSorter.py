"""
Enhanced File Sorter - Organize your messy folders!
Usage: python FileSorter.py <folder_path> [--dry-run]
"""

import os
import shutil
from pathlib import Path
import argparse
from datetime import datetime


class FileSorter:
    """Smart file organizer with multiple sorting strategies."""
    
    FILE_TYPES = {
        'Images': ['.png', '.jpg', '.jpeg', '.gif', '.svg', '.bmp', '.webp', '.ico'],
        'Documents': ['.pdf', '.docx', '.doc', '.txt', '.md', '.rtf', '.odt'],
        'Code': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c', '.go', '.rs'],
        'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2'],
        'Videos': ['.mp4', '.mov', '.avi', '.mkv', '.wmv', '.flv', '.webm'],
        'Music': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.m4a'],
        'Spreadsheets': ['.xlsx', '.xls', '.csv', '.ods'],
        'Presentations': ['.pptx', '.ppt', '.key', '.odp'],
        'Executables': ['.exe', '.msi', '.app', '.dmg', '.deb', '.rpm'],
        'Fonts': ['.ttf', '.otf', '.woff', '.woff2'],
    }
    
    def __init__(self, source_folder, dry_run=False, by_date=False):
        self.source_path = Path(source_folder).resolve()
        self.dry_run = dry_run
        self.by_date = by_date
        self.stats = {
            'moved': 0,
            'skipped': 0,
            'errors': 0
        }
    
    def get_folder_for_extension(self, extension):
        """Determine target folder based on file extension."""
        for folder, extensions in self.FILE_TYPES.items():
            if extension.lower() in extensions:
                return folder
        return 'Others'
    
    def get_date_folder(self, file_path):
        """Get folder name based on file modification date."""
        timestamp = file_path.stat().st_mtime
        date = datetime.fromtimestamp(timestamp)
        return date.strftime('%Y-%m')
    
    def sort_files(self):
        """Main sorting logic."""
        if not self.source_path.exists():
            print(f"❌ Error: {self.source_path} does not exist")
            return
        
        if not self.source_path.is_dir():
            print(f"❌ Error: {self.source_path} is not a directory")
            return
        
        print(f"\n{'🔍 DRY RUN MODE' if self.dry_run else '📂 SORTING FILES'}")
        print(f"Source: {self.source_path}")
        print("=" * 60)
        
        for item in sorted(self.source_path.iterdir()):
            if item.is_file() and not item.name.startswith('.'):
                self._process_file(item)
        
        self._print_summary()
    
    def _process_file(self, file_path):
        """Process a single file."""
        try:
            ext = file_path.suffix
            
            # Determine target folder
            if self.by_date:
                type_folder = self.get_folder_for_extension(ext)
                date_folder = self.get_date_folder(file_path)
                target_folder = self.source_path / type_folder / date_folder
            else:
                folder_name = self.get_folder_for_extension(ext)
                target_folder = self.source_path / folder_name
            
            # Create target path
            target_path = target_folder / file_path.name
            
            # Handle name conflicts
            counter = 1
            while target_path.exists() and target_path != file_path:
                stem = file_path.stem
                target_path = target_folder / f"{stem}_{counter}{ext}"
                counter += 1
            
            # Execute or preview
            if self.dry_run:
                print(f"Would move: {file_path.name} → {target_folder.relative_to(self.source_path)}")
            else:
                target_folder.mkdir(parents=True, exist_ok=True)
                shutil.move(str(file_path), str(target_path))
                print(f"✅ Moved: {file_path.name} → {target_folder.relative_to(self.source_path)}")
            
            self.stats['moved'] += 1
            
        except PermissionError:
            print(f"⚠️  Permission denied: {file_path.name}")
            self.stats['errors'] += 1
        except Exception as e:
            print(f"❌ Error processing {file_path.name}: {e}")
            self.stats['errors'] += 1
    
    def _print_summary(self):
        """Print sorting statistics."""
        print("\n" + "=" * 60)
        print("📊 SUMMARY")
        print("=" * 60)
        print(f"✅ Files moved: {self.stats['moved']}")
        print(f"⚠️  Errors: {self.stats['errors']}")
        
        if self.dry_run:
            print("\n💡 Run without --dry-run to actually move files")


def main():
    parser = argparse.ArgumentParser(
        description="📁 Enhanced File Sorter - Organize your messy folders!",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python FileSorter.py ~/Downloads
  python FileSorter.py ~/Downloads --dry-run
  python FileSorter.py ~/Downloads --by-date
        """
    )
    
    parser.add_argument(
        "folder",
        help="Path to folder to sort"
    )
    
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without moving files"
    )
    
    parser.add_argument(
        "--by-date",
        action="store_true",
        help="Organize files by modification date within type folders"
    )
    
    args = parser.parse_args()
    
    sorter = FileSorter(args.folder, args.dry_run, args.by_date)
    sorter.sort_files()


if __name__ == "__main__":
    main()
