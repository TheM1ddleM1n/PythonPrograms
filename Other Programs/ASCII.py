"""
ASCII Art Generator - Convert images and text to ASCII art
Features: Image to ASCII, text banners, gradient effects
"""

from PIL import Image
import sys
from pathlib import Path


class ASCIIArtGenerator:
    """Generate ASCII art from images and text."""

    # ASCII characters from dark to light
    ASCII_CHARS_DETAILED = " .'`^\",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
    ASCII_CHARS_SIMPLE = " .:-=+*#%@"
    ASCII_CHARS_BLOCKS = " ░▒▓█"

    BANNER_FONTS = {
        'standard': {
            'A': [
                "  ___  ",
                " / _ \\ ",
                "| |_| |",
                "|  _  |",
                "|_| |_|"
            ],
            'B': [
                " _____ ",
                "|  _  \\",
                "| |_| |",
                "|  _ <",
                "|_____/"
            ],
            'C': [
                "  ____ ",
                " / ___|",
                "| |    ",
                "| |___ ",
                " \\____|"
            ],
            # Add more letters as needed - this is a simplified version
        }
    }

    def __init__(self):
        self.width = 100
        self.char_set = self.ASCII_CHARS_SIMPLE

    def image_to_ascii(self, image_path: str, width: int = 100, detailed: bool = False):
        """Convert an image to ASCII art."""
        try:
            # Select character set
            if detailed:
                chars = self.ASCII_CHARS_DETAILED
            else:
                chars = self.ASCII_CHARS_SIMPLE

            # Open and process image
            img = Image.open(image_path)

            # Calculate height to maintain aspect ratio
            aspect_ratio = img.height / img.width
            height = int(width * aspect_ratio * 0.55)  # 0.55 to account for character height

            # Resize image
            img = img.resize((width, height))

            # Convert to grayscale
            img = img.convert('L')

            # Convert pixels to ASCII
            pixels = img.getdata()
            ascii_str = ""

            for i, pixel in enumerate(pixels):
                # Map pixel value (0-255) to character index
                char_index = int((pixel / 255) * (len(chars) - 1))
                ascii_str += chars[char_index]

                # Add newline at end of row
                if (i + 1) % width == 0:
                    ascii_str += "\n"

            return ascii_str

        except FileNotFoundError:
            return f"❌ Error: Image file '{image_path}' not found"
        except Exception as e:
            return f"❌ Error: {e}"

    def text_banner(self, text: str, style: str = 'simple'):
        """Create ASCII art banner from text."""
        text = text.upper()

        if style == 'simple':
            return self._simple_banner(text)
        elif style == 'block':
            return self._block_banner(text)
        elif style == 'shadow':
            return self._shadow_banner(text)
        else:
            return self._simple_banner(text)

    def _simple_banner(self, text: str) -> str:
        """Simple ASCII banner."""
        line1 = " _____ " * len(text)
        line2 = ""
        line3 = ""
        line4 = ""

        for char in text:
            if char == ' ':
                line2 += "       "
                line3 += "       "
                line4 += "       "
            else:
                line2 += f"| {char}   |"
                line3 += "|_____|"
                line4 += "       "

        return f"{line1}\n{line2}\n{line3}"

    def _block_banner(self, text: str) -> str:
        """Block-style banner."""
        result = []
        for char in text:
            if char == ' ':
                result.append("   ")
            else:
                result.append(f"█{char}█")

        return ' '.join(result)

    def _shadow_banner(self, text: str) -> str:
        """Shadow effect banner."""
        line1 = ""
        line2 = ""

        for char in text:
            if char == ' ':
                line1 += "   "
                line2 += "   "
            else:
                line1 += f"{char}  "
                line2 += f" {char} "

        return f"{line1}\n{line2}"

    def gradient_text(self, text: str) -> str:
        """Create gradient ASCII art."""
        chars = self.ASCII_CHARS_BLOCKS
        result = []

        for i, char in enumerate(text):
            if char == ' ':
                result.append(' ')
            else:
                # Cycle through gradient characters
                char_index = i % len(chars)
                result.append(chars[char_index] * 2)

        return ''.join(result)

    def heart(self) -> str:
        """Generate ASCII heart."""
        return """
      ****       ****
    **    **   **    **
   *        ***        *
   *                   *
    *                 *
     *               *
      *             *
       *           *
        *         *
         *       *
          *     *
           *   *
            * *
             *
        """

    def custom_art(self, art_type: str) -> str:
        """Return pre-made ASCII art."""
        arts = {
            'heart': self.heart(),
            'star': """
           *
          ***
         *****
        *******
       *********
      ***********
     *************
      ***********
       *********
        *******
         *****
          ***
           *
            """,
            'smiley': """
        *****
      *       *
     *  o   o  *
    *           *
    *   \\___/   *
     *         *
      *       *
        *****
            """,
            'rocket': """
         /\\
        /  \\
       |    |
       | ** |
      /|    |\\
     / |    | \\
    /  |    |  \\
   /___|    |___\\
       |    |
       |    |
      /|    |\\
     / |    | \\
    /__|    |__\\
            """,
        }

        return arts.get(art_type, "❌ Art type not found")

    def save_to_file(self, ascii_art: str, filename: str):
        """Save ASCII art to a text file."""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(ascii_art)
            print(f"✅ Saved to {filename}")
        except Exception as e:
            print(f"❌ Error saving file: {e}")


def main():
    """Main program interface."""
    generator = ASCIIArtGenerator()

    print("""
    ╔═══════════════════════════════════════╗
    ║    🎨 ASCII ART GENERATOR 🎨         ║
    ╚═══════════════════════════════════════╝
    """)

    while True:
        print("\n" + "=" * 50)
        print("1. Convert Image to ASCII")
        print("2. Create Text Banner")
        print("3. Generate Gradient Text")
        print("4. Pre-made ASCII Art")
        print("5. Exit")
        print("=" * 50)

        choice = input("\nChoose option (1-5): ").strip()

        if choice == "1":
            image_path = input("\nEnter image path: ").strip()
            width = input("Width in characters (default 100): ").strip()
            detailed = input("Use detailed characters? (y/n, default n): ").strip().lower() == 'y'

            width = int(width) if width else 100

            print("\n🎨 Generating ASCII art...\n")
            result = generator.image_to_ascii(image_path, width, detailed)
            print(result)

            save = input("\nSave to file? (y/n): ").strip().lower()
            if save == 'y':
                filename = input("Filename (e.g., output.txt): ").strip()
                generator.save_to_file(result, filename)

        elif choice == "2":
            text = input("\nEnter text for banner: ").strip()
            print("\nStyles: simple, block, shadow")
            style = input("Choose style (default simple): ").strip() or 'simple'

            print("\n" + "=" * 50)
            result = generator.text_banner(text, style)
            print(result)
            print("=" * 50)

            save = input("\nSave to file? (y/n): ").strip().lower()
            if save == 'y':
                filename = input("Filename: ").strip()
                generator.save_to_file(result, filename)

        elif choice == "3":
            text = input("\nEnter text: ").strip()
            result = generator.gradient_text(text)
            print(f"\n{result}\n")

        elif choice == "4":
            print("\nAvailable: heart, star, smiley, rocket")
            art_type = input("Choose art: ").strip().lower()
            result = generator.custom_art(art_type)
            print(result)

        elif choice == "5":
            print("\n🎨 Keep creating! Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
        sys.exit(0)
