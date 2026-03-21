import random
from colorama import Back, Fore, Style, init

init(autoreset=True)

WORD_LENGTH = 5
MAX_GUESSES = 6

ANSWERS = [
    "abbey", "aloft", "amber", "audio", "birch", "bison", "blaze", "blunt",
    "boxer", "brave", "brine", "camel", "civic", "cloud", "coral", "crane",
    "crisp", "debut", "delta", "denim", "dwarf", "eagle", "elbow", "ember",
    "ethos", "evade", "expel", "feign", "flair", "flame", "frost", "fudge",
    "ghost", "gloom", "grace", "grail", "haste", "haven", "honey", "husky",
    "icing", "igloo", "inlet", "irony", "ivory", "jazzy", "jewel", "joker",
    "joust", "karma", "kebab", "knack", "kneel", "laser", "lemon", "lodge",
    "lusty", "lymph", "mango", "maple", "micro", "mirth", "month", "moose",
    "naval", "night", "noble", "noise", "notch", "ocean", "olive", "optic",
    "otter", "oxide", "peace", "perch", "piano", "pilot", "pixel", "pixie",
    "prism", "qualm", "queen", "quill", "quirk", "quota", "radar", "raven",
    "reign", "risky", "rivet", "river", "rogue", "rusty", "scald", "scone",
    "shore", "sieve", "snowy", "solar", "stone", "swift", "talon", "tiger",
    "tonic", "trail", "trout", "truce", "ultra", "umbra", "unify", "usher",
    "vapor", "venom", "verse", "vigil", "viola", "vouch", "wafer", "waltz",
    "water", "witty", "xenon", "yacht", "yeast", "youth", "zebra", "zesty",
    "zippy",
]

EXTRA = {
    "about", "above", "abuse", "actor", "acute", "admit", "adopt", "adult",
    "after", "again", "agent", "agree", "ahead", "alarm", "alert", "alien",
    "alike", "alive", "alone", "along", "alter", "angel", "anger", "angle",
    "annex", "annoy", "apart", "apple", "apply", "argue", "arise", "array",
    "arrow", "aside", "atone", "awful", "badge", "baker", "basic", "basin",
    "batch", "beach", "beard", "beast", "bench", "black", "blade", "bland",
    "blank", "blast", "bleed", "blend", "bless", "blink", "blood", "bloom",
    "blown", "board", "bogus", "bound", "brain", "brand", "brass", "bread",
    "break", "breed", "brick", "bride", "brief", "brink", "broke", "brook",
    "broom", "brown", "build", "built", "bulge", "bully", "bunch", "buyer",
    "cabin", "carry", "carve", "catch", "cause", "cease", "chain", "chair",
    "chalk", "chant", "chaos", "charm", "chart", "chase", "cheap", "cheat",
    "cheek", "cheer", "chess", "chest", "chief", "chill", "china", "choke",
    "chord", "chose", "chunk", "claim", "clamp", "clash", "class", "clerk",
    "click", "cliff", "cling", "clink", "clock", "clone", "close", "cloth",
    "coach", "coast", "comet", "comic", "conch", "couch", "cough", "could",
    "count", "cover", "covet", "crack", "craft", "crash", "creak", "creed",
    "creep", "crest", "croak", "crook", "cross", "crowd", "crown", "crude",
    "cruel", "crush", "crust", "curly", "curve", "daily", "daisy", "dandy",
    "dated", "death", "decoy", "delay", "depth", "derby", "devil", "diary",
    "digit", "dirty", "disco", "ditch", "dizzy", "dodge", "doubt", "dough",
    "drain", "drama", "drawl", "drawn", "dread", "dream", "dress", "dried",
    "drift", "drink", "drive", "drove", "drown", "drunk", "dusty", "early",
    "earth", "eight", "elite", "empty", "enact", "enjoy", "enter", "entry",
    "epoch", "equal", "erect", "error", "essay", "ethic", "every", "evict",
    "exact", "exist", "extra", "fable", "facet", "faith", "false", "fancy",
    "fatal", "fatty", "fault", "favor", "feast", "feral", "fever", "fiend",
    "fiery", "fifth", "fight", "filth", "final", "first", "fixed", "flank",
    "flask", "flesh", "flick", "fling", "float", "flock", "flood", "flour",
    "flown", "focal", "force", "forge", "forte", "found", "frank", "fraud",
    "freak", "fresh", "front", "froze", "fungi", "funky", "funny", "furry",
    "gable", "gauze", "giddy", "girth", "given", "gland", "glare", "glass",
    "glaze", "gleam", "glide", "glint", "globe", "gloss", "glove", "going",
    "goose", "gouge", "gourd", "grain", "grand", "grasp", "grass", "grate",
    "grave", "graze", "greed", "green", "greet", "grief", "grime", "grind",
    "gripe", "groan", "grout", "growl", "grown", "grump", "guard", "guile",
    "guise", "gulch", "habit", "hairy", "halve", "handy", "harsh", "haunt",
    "heady", "heard", "heart", "heavy", "hedge", "heist", "hence", "hippo",
    "hitch", "hoist", "holly", "horse", "hotel", "hound", "house", "human",
    "humid", "hurry", "ideal", "index", "indie", "inert", "ingot", "inner",
    "input", "inter", "intro", "irate", "jiffy", "jolly", "jumpy", "kayak",
    "khaki", "knife", "knock", "known", "kudos", "lapse", "latch", "laugh",
    "layer", "leaky", "learn", "lease", "leave", "ledge", "legal", "level",
    "linen", "liner", "lofty", "logic", "loopy", "lower", "loyal", "lucky",
    "lunar", "lunch", "lying", "magic", "major", "maker", "manly", "manor",
    "march", "marsh", "match", "mayor", "meant", "mercy", "merit", "messy",
    "metal", "might", "mimic", "mince", "minor", "misty", "mixed", "model",
    "moody", "morph", "mossy", "motif", "motto", "mourn", "mucky", "muddy",
    "murky", "musty", "nadir", "nasty", "nervy", "noisy", "nomad", "order",
    "other", "ought", "outer", "paint", "pasta", "pasty", "patch", "pause",
    "peach", "penal", "peril", "petal", "petty", "phase", "phone", "photo",
    "picky", "pitch", "pivot", "plain", "plank", "plant", "plead", "plumb",
    "plump", "plush", "point", "poker", "polar", "poppy", "porch", "power",
    "prank", "prawn", "press", "price", "pride", "print", "probe", "prowl",
    "prude", "pulse", "punch", "pupil", "puppy", "purse", "quick", "quiet",
    "rabbi", "rabid", "rainy", "rally", "rapid", "raspy", "ratty", "reach",
    "ready", "realm", "regal", "repay", "repel", "resin", "revel", "rider",
    "ridge", "rifle", "right", "rigid", "risen", "rival", "roast", "rocky",
    "roman", "roomy", "rouge", "rough", "rowdy", "rugby", "ruler", "rumor",
    "rural", "sadly", "saint", "sassy", "savor", "savvy", "scalp", "scant",
    "scare", "scene", "scoff", "scoop", "scope", "score", "scorn", "scout",
    "scowl", "scrap", "screw", "seedy", "serve", "setup", "shame", "shape",
    "share", "shark", "sharp", "sheep", "sheer", "shelf", "shell", "shift",
    "shine", "shirt", "shoot", "shout", "shove", "shown", "shrub", "since",
    "sixth", "sixty", "skate", "skull", "skunk", "sleep", "sleet", "slice",
    "slick", "slide", "slope", "small", "smash", "smear", "smell", "smoke",
    "snack", "snail", "snake", "snare", "sneak", "snide", "sniff", "solid",
    "sonic", "sorry", "south", "space", "spare", "spark", "spear", "speck",
    "spell", "spend", "spill", "spine", "spite", "spoke", "spoon", "sport",
    "spray", "spunk", "squad", "squat", "stack", "staff", "stage", "stain",
    "stalk", "stall", "stamp", "stand", "stark", "start", "stash", "state",
    "steak", "steal", "steam", "steel", "steep", "steer", "stern", "stiff",
    "still", "sting", "stock", "stomp", "stood", "stool", "store", "storm",
    "story", "stout", "strap", "straw", "stray", "strip", "strut", "stuck",
    "study", "stump", "stunk", "stunt", "style", "suave", "sugar", "suite",
    "sunny", "surge", "swamp", "swear", "sweat", "sweep", "sweet", "swept",
    "swipe", "swirl", "swoop", "sword", "syrup", "tabby", "taste", "taunt",
    "tense", "tepid", "theft", "theme", "thick", "think", "thorn", "those",
    "threw", "throw", "thump", "tidal", "tired", "titan", "today", "topic",
    "torch", "total", "toxic", "train", "trawl", "tread", "trend", "trick",
    "tried", "trove", "truck", "truly", "trunk", "trust", "truth", "tumor",
    "tuner", "tunic", "tutor", "twang", "tweak", "twice", "twist", "tying",
    "under", "until", "unzip", "upset", "urban", "usual", "vague", "valor",
    "valve", "vault", "viral", "vista", "vital", "vivid", "vocal", "vodka",
    "vogue", "vowel", "wacky", "waste", "watch", "weave", "wedge", "weird",
    "whale", "while", "white", "whole", "widen", "windy", "woman", "wonky",
    "world", "worry", "worse", "worst", "worth", "would", "wound", "wrath",
    "wreck", "wrest", "wring", "wrist", "wrong", "yearn", "yield", "young",
    "yours", "zippy",
}

VALID_WORDS = set(ANSWERS) | EXTRA

GREEN  = Back.GREEN + Fore.WHITE + Style.BRIGHT
YELLOW = Back.YELLOW + Fore.BLACK + Style.BRIGHT
GREY   = Back.LIGHTBLACK_EX + Fore.WHITE
RESET  = Style.RESET_ALL


def _colour_tile(letter: str, status: str) -> str:
    letter = letter.upper()
    if status == "green":
        return f"{GREEN} {letter} {RESET}"
    if status == "yellow":
        return f"{YELLOW} {letter} {RESET}"
    return f"{GREY} {letter} {RESET}"


def _empty_tile() -> str:
    return f"{Back.WHITE + Fore.BLACK}   {RESET}"


class WordleGame:
    SEPARATOR = "─" * 33

    def __init__(self) -> None:
        self.answer = random.choice(ANSWERS)
        self.guesses: list[list[tuple[str, str]]] = []
        self.won = False

    def check_guess(self, guess: str) -> list[tuple[str, str]]:
        statuses = [""] * WORD_LENGTH
        remaining = list(self.answer)

        for i, letter in enumerate(guess):
            if letter == self.answer[i]:
                statuses[i] = "green"
                remaining[i] = ""

        for i, letter in enumerate(guess):
            if statuses[i]:
                continue
            if letter in remaining:
                statuses[i] = "yellow"
                remaining[remaining.index(letter)] = ""
            else:
                statuses[i] = "grey"

        return list(zip(guess, statuses))

    def _board(self) -> None:
        """Print the full 6-row board."""
        print()
        for i in range(MAX_GUESSES):
            if i < len(self.guesses):
                row = "".join(_colour_tile(l, s) for l, s in self.guesses[i])
            else:
                row = "".join(_empty_tile() for _ in range(WORD_LENGTH))
            print(f"  {row}")
        print()

    def _keyboard(self) -> None:
        """Print a colour-coded QWERTY hint row."""
        status_map: dict[str, str] = {}
        for result in self.guesses:
            for letter, status in result:
                current = status_map.get(letter)
                if current == "green":
                    continue
                if status == "green" or current is None:
                    status_map[letter] = status
                elif status == "yellow" and current == "grey":
                    status_map[letter] = status

        for row in ("qwertyuiop", "asdfghjkl", "zxcvbnm"):
            print("  ", end="")
            for letter in row:
                status = status_map.get(letter)
                if status:
                    print(_colour_tile(letter, status), end="")
                else:
                    print(f" {letter.upper()} ", end="")
            print()
        print()

    def play(self) -> None:
        """Run the game loop."""
        print("\n" + "=" * 33)
        print("🟩 WORDLE")
        print("=" * 33)
        print("Guess the 5-letter word in 6 tries.")
        print()
        print("🟩 Correct letter, correct spot")
        print("🟨 Correct letter, wrong spot")
        print("⬛ Letter not in the word")
        print(self.SEPARATOR)

        while len(self.guesses) < MAX_GUESSES:
            self._board()
            self._keyboard()

            remaining = MAX_GUESSES - len(self.guesses)
            raw = input(
                f"  Guess {len(self.guesses) + 1}/{MAX_GUESSES}"
                f" ({remaining} left) > "
            ).strip().lower()

            if len(raw) != WORD_LENGTH:
                print(f"\n  ⚠️  Must be exactly {WORD_LENGTH} letters.\n")
                continue
            if not raw.isalpha():
                print("\n  ⚠️  Letters only, please.\n")
                continue
            if raw not in VALID_WORDS:
                print("\n  ⚠️  Not in word list. Try again.\n")
                continue

            result = self.check_guess(raw)
            self.guesses.append(result)

            if all(s == "green" for _, s in result):
                self.won = True
                break

        self._board()
        self._show_result()

    def _show_result(self) -> None:
        """Print the win or loss summary."""
        print(self.SEPARATOR)
        if self.won:
            n = len(self.guesses)
            msgs = {
                1: "🏆 Extraordinary — hole in one!",
                2: "🎉 Brilliant! Got it in 2.",
                3: "😎 Sorted! Got it in 3.",
                4: "👍 Nice one — got it in 4.",
                5: "😅 Phew — squeaked it in 5.",
                6: "😤 Just in time — got it in 6!",
            }
            print(msgs.get(n, f"✅ Got it in {n}."))
        else:
            print(f"💀 Hard luck! The word was: {self.answer.upper()}")
        print(self.SEPARATOR)


def main() -> None:
    while True:
        game = WordleGame()
        game.play()

        again = input("\n🔄 Play again? (y/n): ").strip().lower()
        if again != "y":
            print("\n👋 Thanks for playing!")
            break


if __name__ == "__main__":
    main()
