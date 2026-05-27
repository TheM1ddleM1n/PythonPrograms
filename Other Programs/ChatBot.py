import random
import json
import os
from datetime import datetime
from pathlib import Path


class Chatbot:
    
    def __init__(self, responses_file="chatbot_responses.json"):
        self.responses_file = responses_file
        self.conversation_history = []
        self.user_name = None
        self.session_start = datetime.now()
        self.user_data_file = "user_data.json"
        self.custom_responses = {}
        self.load_responses()
        self.ensure_responses_file()
        self.load_user_data()
    
    def ensure_responses_file(self):
        if not os.path.exists(self.responses_file):
            default_responses = {
                "greeting": {
                    "patterns": ["hello", "hi", "hey", "greetings", "what's up"],
                    "responses": [
                        "Hi there! How can I help you today?",
                        "Hello! Nice to meet you!",
                        "Hey! What's on your mind?",
                        "Greetings! How are you doing?"
                    ]
                },
                "name": {
                    "patterns": ["my name is", "i'm", "call me", "i am"],
                    "responses": [
                        "Nice to meet you, {name}! I'll remember that.",
                        "Great name, {name}! What can I do for you?",
                        "Pleased to meet you, {name}!"
                    ]
                },
                "how_are_you": {
                    "patterns": ["how are you", "how do you feel", "how's it going"],
                    "responses": [
                        "I'm doing great, thanks for asking!",
                        "Fantastic! Ready to chat.",
                        "Couldn't be better! How about you?",
                        "I'm excellent! How can I help?"
                    ]
                },
                "user_status": {
                    "patterns": ["i'm fine", "i'm good", "i'm great", "doing well", "doing good"],
                    "responses": [
                        "That's wonderful to hear!",
                        "Glad you're doing well!",
                        "Awesome! Let's have a great chat.",
                        "That makes me happy!"
                    ]
                },
                "name_query": {
                    "patterns": ["what's your name", "who are you", "your name"],
                    "responses": [
                        "I'm ChatBot, your friendly AI assistant!",
                        "You can call me ChatBot.",
                        "I'm ChatBot, here to help!"
                    ]
                },
                "help": {
                    "patterns": ["help", "what can you do", "capabilities", "commands"],
                    "responses": [
                        "I can chat with you, answer questions, and remember your name! Try asking me about Python, math, or just chat!",
                        "I'm here to have conversations! You can ask me questions or just say hi.",
                        "I can assist with general questions and have friendly conversations. What would you like to know?"
                    ]
                },
                "python": {
                    "patterns": ["python", "coding", "programming", "code"],
                    "responses": [
                        "Python is awesome! It's great for beginners and professionals alike.",
                        "I love Python! It's one of the most popular programming languages.",
                        "Python is perfect for learning programming. Do you want to know more?"
                    ]
                },
                "bye": {
                    "patterns": ["bye", "goodbye", "see you", "farewell", "exit"],
                    "responses": [
                        "Goodbye! It was nice chatting with you!",
                        "See you later! Have an amazing day!",
                        "Bye! Come back anytime!",
                        "Farewell, friend!"
                    ]
                },
                "thanks": {
                    "patterns": ["thanks", "thank you", "appreciate", "thx"],
                    "responses": [
                        "You're welcome!",
                        "Happy to help!",
                        "Anytime! That's what I'm here for.",
                        "My pleasure!"
                    ]
                },
                "default": {
                    "patterns": [],
                    "responses": [
                        "That's interesting! Tell me more.",
                        "I'm not sure about that, but it sounds cool!",
                        "Hmm, I'd love to learn more about that.",
                        "Can you rephrase that? I want to make sure I understand.",
                        "That's a great point! Anything else on your mind?"
                    ]
                }
            }
            
            with open(self.responses_file, "w") as f:
                json.dump(default_responses, f, indent=2)
            print(f"Created default responses file: {self.responses_file}\n")
    
    def load_responses(self):
        try:
            with open(self.responses_file, "r") as f:
                self.response_patterns = json.load(f)
        except FileNotFoundError:
            print(f"Warning: {self.responses_file} not found. Using defaults.\n")
            self.response_patterns = {}
    
    def load_user_data(self):
        try:
            with open(self.user_data_file, "r") as f:
                self.user_profiles = json.load(f)
        except FileNotFoundError:
            self.user_profiles = {}
    
    def save_user_data(self):
        with open(self.user_data_file, "w") as f:
            json.dump(self.user_profiles, f, indent=2)
    
    def extract_name(self, user_input):
        name_triggers = ["my name is", "i'm", "call me", "i am"]
        
        for trigger in name_triggers:
            if trigger in user_input:
                name = user_input.split(trigger)[-1].strip()
                name = name.rstrip('.!?').strip()
                if len(name) > 1 and len(name) < 50:
                    return name.title()
        
        return None
    
    def find_response(self, user_input):
        user_input_lower = user_input.lower()
        matched_response = None
        is_direct_match = False
        
        extracted_name = self.extract_name(user_input_lower)
        if extracted_name:
            self.user_name = extracted_name
            response_template = random.choice(
                self.response_patterns.get("name", {}).get("responses", [])
            )
            return response_template.format(name=self.user_name), True
        
        for category, data in self.response_patterns.items():
            patterns = data.get("patterns", [])
            responses = data.get("responses", [])
            
            if not patterns:
                continue
            
            for pattern in patterns:
                if pattern in user_input_lower:
                    matched_response = random.choice(responses)
                    is_direct_match = True
                    break
            
            if matched_response:
                break
        
        if not matched_response:
            matched_response = random.choice(
                self.response_patterns.get("default", {}).get("responses", [])
            )
            is_direct_match = False
        
        if self.user_name and is_direct_match:
            if random.random() < 0.2:
                matched_response = f"{matched_response} {self.user_name}?"
        
        return matched_response, is_direct_match
    
    def display_help(self):
        help_text = """
╔════════════════════════════════════════════════════════════╗
║                    CHATBOT HELP & COMMANDS                 ║
╚════════════════════════════════════════════════════════════╝

CONVERSATION COMMANDS:
  help       - Show this help message
  history    - Show current conversation
  clear      - Clear conversation history
  save       - Save conversation to file
  load       - Load previous conversation
  delete     - Delete a saved conversation

USER & PROFILE COMMANDS:
  profile    - View your profile
  setname    - Change your name
  stats      - View chat statistics
  mood       - Tell me your mood
  interests  - Set your interests

RESPONSE MANAGEMENT:
  learn      - Teach me a custom response
  forget     - Delete a custom response
  responses  - List all available responses
  reload     - Reload responses from file

SYSTEM COMMANDS:
  time       - Show current time
  date       - Show current date
  session    - Show session info
  search     - Search conversation history
  export     - Export conversation as CSV
  import     - Import conversation from file
  reset      - Reset all data
  about      - About this chatbot
  quit       - Exit the chatbot

JOKE & FUN COMMANDS:
  joke       - Tell me a joke
  quote      - Show a random quote
  fact       - Tell me a random fact
  flip       - Flip a coin
  roll       - Roll a dice
  rand       - Random number (e.g., 'rand 1 100')

QUICK COMMANDS:
  ?          - Show quick command list
  !          - Repeat last message
  @          - Show unread commands
        """
        print(help_text)
    
    def display_quick_commands(self):
        quick = """
╔═══════════════════════════════════════════════════════╗
║            QUICK COMMAND REFERENCE                    ║
╚═══════════════════════════════════════════════════════╝

help      save      load      history   delete
profile   setname   stats     mood      interests
learn     forget    responses reload    
time      date      session   search    export
joke      quote     fact      flip      roll
quit      clear     about
        """
        print(quick)
    
    def cmd_joke(self):
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "How many programmers does it take to change a light bulb? None, that's a hardware problem!",
            "Why did the developer go broke? Because he used up all his cache!",
            "What's a programmer's favorite hangout place? Foo Bar!",
            "Why do Java developers wear glasses? Because they don't C#!",
            "How many SQL developers does it take to change a light bulb? None, you just alter the table.",
            "Why did the Python programmer get locked out? Because he forgot the key!",
            "What do programmers eat when they get hungry? Stack Overflow!"
        ]
        print(f"Bot: {random.choice(jokes)}\n")
    
    def cmd_quote(self):
        quotes = [
            "The only way to do great work is to love what you do. - Steve Jobs",
            "Innovation distinguishes between a leader and a follower. - Steve Jobs",
            "Life is what happens when you're busy making other plans. - John Lennon",
            "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
            "It is during our darkest moments that we must focus to see the light. - Aristotle",
            "The only impossible journey is the one you never begin. - Tony Robbins",
            "Success is not final, failure is not fatal. - Winston Churchill"
        ]
        print(f"Bot: {random.choice(quotes)}\n")
    
    def cmd_fact(self):
        facts = [
            "Honey never spoils and can last thousands of years!",
            "A group of flamingos is called a 'flamboyance'!",
            "Bananas are berries, but strawberries aren't!",
            "Octopuses have three hearts!",
            "A day on Venus is longer than its year!",
            "Sharks predate dinosaurs by 200 million years!",
            "Your body contains about 37.2 trillion cells!"
        ]
        print(f"Bot: {random.choice(facts)}\n")
    
    def cmd_flip(self):
        result = random.choice(["Heads", "Tails"])
        print(f"Bot: I flipped a coin... {result}!\n")
    
    def cmd_roll(self):
        result = random.randint(1, 6)
        print(f"Bot: 🎲 You rolled a {result}!\n")
    
    def cmd_rand(self, user_input):
        try:
            parts = user_input.split()
            if len(parts) == 3:
                start = int(parts[1])
                end = int(parts[2])
                result = random.randint(start, end)
                print(f"Bot: Random number between {start} and {end}: {result}\n")
            else:
                print("Bot: Usage: rand <start> <end>\n")
        except:
            print("Bot: Invalid input! Use: rand 1 100\n")
    
    def cmd_time(self):
        current_time = datetime.now().strftime("%H:%M:%S")
        print(f"Bot: Current time: {current_time}\n")
    
    def cmd_date(self):
        current_date = datetime.now().strftime("%A, %B %d, %Y")
        print(f"Bot: Today is {current_date}\n")
    
    def cmd_session(self):
        duration = datetime.now() - self.session_start
        hours, remainder = divmod(int(duration.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        
        info = f"""
╔════════════════════════════════════════════════════════════╗
║                     SESSION INFORMATION                    ║
╚════════════════════════════════════════════════════════════╝
Started:           {self.session_start.strftime("%Y-%m-%d %H:%M:%S")}
Duration:          {hours}h {minutes}m {seconds}s
Messages Sent:     {len([m for m in self.conversation_history if m['speaker'] == 'user'])}
Messages Received: {len([m for m in self.conversation_history if m['speaker'] == 'bot'])}
User Name:         {self.user_name if self.user_name else "Not set"}
        """
        print(info)
    
    def cmd_profile(self):
        if not self.user_name:
            print("Bot: You haven't set your name yet! Use 'setname' to set it.\n")
            return
        
        profile_data = self.user_profiles.get(self.user_name, {})
        
        profile_text = f"""
╔════════════════════════════════════════════════════════════╗
║                    YOUR PROFILE                            ║
╚════════════════════════════════════════════════════════════╝
Name:              {self.user_name}
Mood:              {profile_data.get('mood', 'Not set')}
Interests:         {', '.join(profile_data.get('interests', ['None set']))}
Messages Sent:     {profile_data.get('messages_sent', 0)}
Last Visited:      {profile_data.get('last_visited', 'First time!')}
        """
        print(profile_text)
    
    def cmd_setname(self):
        new_name = input("Bot: What's your new name? ").strip().title()
        if new_name and len(new_name) > 1:
            self.user_name = new_name
            if new_name not in self.user_profiles:
                self.user_profiles[new_name] = {"mood": "happy", "interests": []}
            self.save_user_data()
            print(f"Bot: Nice! I'll call you {new_name} from now on.\n")
        else:
            print("Bot: Invalid name! Please try again.\n")
    
    def cmd_mood(self):
        moods = ["happy", "sad", "excited", "tired", "confused", "motivated"]
        mood = input("Bot: How are you feeling? (happy/sad/excited/tired/confused/motivated): ").strip().lower()
        
        if mood in moods:
            if self.user_name:
                if self.user_name not in self.user_profiles:
                    self.user_profiles[self.user_name] = {}
                self.user_profiles[self.user_name]["mood"] = mood
                self.save_user_data()
            print(f"Bot: I hope things get better if you're feeling {mood}! 💙\n")
        else:
            print("Bot: That's not a valid mood. Try: happy, sad, excited, tired, confused, or motivated.\n")
    
    def cmd_interests(self):
        interests_input = input("Bot: What are your interests? (comma-separated): ").strip()
        interests = [i.strip() for i in interests_input.split(",")]
        
        if self.user_name:
            if self.user_name not in self.user_profiles:
                self.user_profiles[self.user_name] = {}
            self.user_profiles[self.user_name]["interests"] = interests
            self.save_user_data()
            print(f"Bot: Great! I'll remember your interests: {', '.join(interests)}\n")
        else:
            print("Bot: Please set your name first using 'setname'\n")
    
    def cmd_learn(self):
        trigger = input("Bot: What trigger word/phrase should activate this? ").strip().lower()
        response = input("Bot: What should I respond with? ").strip()
        
        if trigger and response
    def cmd_learn(self):
        trigger = input("Bot: What trigger word/phrase should activate this? ").strip().lower()
        response = input("Bot: What should I respond with? ").strip()
        
        if trigger and response:
            self.custom_responses[trigger] = response
            print(f"Bot: Learned! I'll respond to '{trigger}' with '{response}'\n")
        else:
            print("Bot: Invalid input! Please provide both trigger and response.\n")
    
    def cmd_forget(self):
        if not self.custom_responses:
            print("Bot: I haven't learned anything custom yet!\n")
            return
        
        print("Bot: What should I forget?")
        for i, trigger in enumerate(self.custom_responses.keys(), 1):
            print(f"  {i}. {trigger}")
        
        try:
            choice = int(input("Bot: Enter number (0 to cancel): "))
            if choice == 0:
                return
            trigger = list(self.custom_responses.keys())[choice - 1]
            del self.custom_responses[trigger]
            print(f"Bot: Forgotten '{trigger}'!\n")
        except:
            print("Bot: Invalid choice!\n")
    
    def cmd_responses(self):
        print("\n╔════════════════════════════════════════════════════════════╗")
        print("║              AVAILABLE RESPONSE CATEGORIES                ║")
        print("╚════════════════════════════════════════════════════════════╝\n")
        
        for category in self.response_patterns.keys():
            patterns = self.response_patterns[category].get("patterns", [])
            count = len(patterns)
            print(f"{category.upper():<20} ({count} patterns)")
            if patterns:
                print(f"  Triggers: {', '.join(patterns[:3])}")
                if len(patterns) > 3:
                    print(f"            ... and {len(patterns) - 3} more")
            print()
        
        if self.custom_responses:
            print("CUSTOM RESPONSES:")
            for trigger in self.custom_responses.keys():
                print(f"  - {trigger}")
            print()
    
    def cmd_reload(self):
        self.load_responses()
        print("Bot: Response patterns reloaded!\n")
    
    def cmd_stats(self):
        total_user_msgs = len([m for m in self.conversation_history if m['speaker'] == 'user'])
        total_bot_msgs = len([m for m in self.conversation_history if m['speaker'] == 'bot'])
        total_words_sent = sum(len(m['message'].split()) for m in self.conversation_history if m['speaker'] == 'user')
        
        stats_text = f"""
╔════════════════════════════════════════════════════════════╗
║                   CHAT STATISTICS                          ║
╚════════════════════════════════════════════════════════════╝
Total Messages:     {total_user_msgs + total_bot_msgs}
Your Messages:      {total_user_msgs}
My Messages:        {total_bot_msgs}
Words You've Sent:  {total_words_sent}
Average Message:    {total_words_sent // max(total_user_msgs, 1)} words
Custom Responses:   {len(self.custom_responses)}
        """
        print(stats_text)
    
    def cmd_search(self):
        query = input("Bot: Search for what? ").strip().lower()
        
        results = [m for m in self.conversation_history 
                   if query in m['message'].lower()]
        
        if not results:
            print(f"Bot: No messages found containing '{query}'\n")
            return
        
        print(f"\nBot: Found {len(results)} message(s):\n")
        for msg in results[-5:]:
            print(f"[{msg['timestamp']}] {msg['speaker'].upper()}: {msg['message']}")
        print()
    
    def cmd_display_history(self):
        if not self.conversation_history:
            print("\n(No conversation history yet)\n")
            return
        
        print("\n" + "=" * 60)
        print("CONVERSATION HISTORY")
        print("=" * 60)
        for message in self.conversation_history:
            speaker = message["speaker"].upper()
            text = message["message"]
            timestamp = message["timestamp"]
            print(f"[{timestamp}] {speaker}: {text}")
        print("=" * 60 + "\n")
    
    def cmd_clear_history(self):
        confirm = input("Bot: Really clear all history? (yes/no): ").strip().lower()
        if confirm == "yes":
            self.conversation_history.clear()
            print("Bot: Conversation history cleared!\n")
        else:
            print("Bot: Cancelled.\n")
    
    def cmd_save_conversation(self):
        if not self.conversation_history:
            print("Bot: Nothing to save!\n")
            return
        
        filename = f"chat_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        chat_data = {
            "started_at": self.session_start.isoformat(),
            "ended_at": datetime.now().isoformat(),
            "user_name": self.user_name,
            "messages": self.conversation_history
        }
        
        with open(filename, "w") as f:
            json.dump(chat_data, f, indent=2)
        
        print(f"Bot: Conversation saved to '{filename}'\n")
        return filename
    
    def cmd_export_csv(self):
        if not self.conversation_history:
            print("Bot: Nothing to export!\n")
            return
        
        filename = f"chat_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        
        with open(filename, "w") as f:
            f.write("timestamp,speaker,message\n")
            for msg in self.conversation_history:
                timestamp = msg['timestamp']
                speaker = msg['speaker']
                message = msg['message'].replace(',', ';').replace('\n', ' ')
                f.write(f"{timestamp},{speaker},{message}\n")
        
        print(f"Bot: Exported to '{filename}'\n")
    
    def cmd_load_conversation(self):
        files = [f for f in os.listdir() if f.startswith("chat_history_") and f.endswith(".json")]
        
        if not files:
            print("Bot: No saved conversations found!\n")
            return
        
        print("Bot: Available conversations:")
        for i, f in enumerate(files, 1):
            size = os.path.getsize(f) // 1024
            print(f"  {i}. {f} ({size}KB)")
        
        try:
            choice = int(input("Bot: Load which one? (0 to cancel): "))
            if choice == 0:
                return
            
            with open(files[choice - 1], "r") as f:
                data = json.load(f)
                self.conversation_history = data.get("messages", [])
                self.user_name = data.get("user_name")
                print(f"Bot: Loaded {len(self.conversation_history)} messages!\n")
        except:
            print("Bot: Invalid choice!\n")
    
    def cmd_delete_conversation(self):
        files = [f for f in os.listdir() if f.startswith("chat_history_") and f.endswith(".json")]
        
        if not files:
            print("Bot: No saved conversations found!\n")
            return
        
        print("Bot: Conversations to delete:")
        for i, f in enumerate(files, 1):
            print(f"  {i}. {f}")
        
        try:
            choice = int(input("Bot: Delete which one? (0 to cancel): "))
            if choice == 0:
                return
            
            os.remove(files[choice - 1])
            print(f"Bot: Deleted '{files[choice - 1]}'!\n")
        except:
            print("Bot: Invalid choice!\n")
    
    def cmd_reset(self):
        confirm = input("Bot: This will delete ALL data! Really reset? (yes/no): ").strip().lower()
        if confirm == "yes":
            self.conversation_history.clear()
            self.custom_responses.clear()
            self.user_name = None
            self.user_profiles.clear()
            self.save_user_data()
            print("Bot: All data reset!\n")
        else:
            print("Bot: Cancelled.\n")
    
    def cmd_about(self):
        about_text = """
╔════════════════════════════════════════════════════════════╗
║                   ABOUT THIS CHATBOT                       ║
╚════════════════════════════════════════════════════════════╝

Simple Chatbot v2.0
A conversational AI with custom learning capabilities.

FEATURES:
✓ Natural language understanding
✓ Custom response learning
✓ User profiles & preferences
✓ Conversation history tracking
✓ Save/load conversations
✓ Fun commands (jokes, quotes, facts)
✓ Statistics & analytics
✓ Session management

CREATED BY: TheM1ddleM1n
REPOSITORY: PythonProgramsV3

Type 'help' to see all commands!
        """
        print(about_text)
    
    def run(self):
        print("\n" + "=" * 60)
        print(" " * 15 + "WELCOME TO SIMPLE CHATBOT V2.0")
        print("=" * 60)
        print("\nType 'help' for commands or '?' for quick reference")
        print("Type 'quit' to exit.\n")
        
        last_response = None
        
        while True:
            try:
                user_input = input("You: ").strip()
                
                if not user_input:
                    continue
                
                if user_input.lower() == "quit":
                    print("\nBot: Saving your conversation...")
                    self.cmd_save_conversation()
                    print("Bot: Goodbye! It was nice chatting with you!")
                    break
                
                elif user_input.lower() == "?":
                    self.display_quick_commands()
                    continue
                
                elif user_input.lower() == "!":
                    if last_response:
                        print(f"Bot: {last_response}\n")
                    else:
                        print("Bot: Nothing to repeat!\n")
                    continue
                
                elif user_input.lower() == "help":
                    self.display_help()
                    continue
                
                elif user_input.lower() == "history":
                    self.cmd_display_history()
                    continue
                
                elif user_input.lower() == "clear":
                    self.cmd_clear_history()
                    continue
                
                elif user_input.lower() == "save":
                    self.cmd_save_conversation()
                    continue
                
                elif user_input.lower() == "load":
                    self.cmd_load_conversation()
                    continue
                
                elif user_input.lower() == "delete":
                    self.cmd_delete_conversation()
                    continue
                
                elif user_input.lower() == "profile":
                    self.cmd_profile()
                    continue
                
                elif user_input.lower() == "setname":
                    self.cmd_setname()
                    continue
                
                elif user_input.lower() == "stats":
                    self.cmd_stats()
                    continue
                
                elif user_input.lower() == "mood":
                    self.cmd_mood()
                    continue
                
                elif user_input.lower() == "interests":
                    self.cmd_interests()
                    continue
                
                elif user_input.lower() == "learn":
                    self.cmd_learn()
                    continue
                
                elif user_input.lower() == "forget":
                    self.cmd_forget()
                    continue
                
                elif user_input.lower() == "responses":
                    self.cmd_responses()
                    continue
                
                elif user_input.lower() == "reload":
                    self.cmd_reload()
                    continue
                
                elif user_input.lower() == "joke":
                    self.cmd_joke()
                    continue
                
                elif user_input.lower() == "quote":
                    self.cmd_quote()
                    continue
                
                elif user_input.lower() == "fact":
                    self.cmd_fact()
                    continue
                
                elif user_input.lower() == "flip":
                    self.cmd_flip()
                    continue
                
                elif user_input.lower() == "roll":
                    self.cmd_roll()
                    continue
                
                elif user_input.lower().startswith("rand"):
                    self.cmd_rand(user_input)
                    continue
                
                elif user_input.lower() == "time":
                    self.cmd_time()
                    continue
                
                elif user_input.lower() == "date":
                    self.cmd_date()
                    continue
                
                elif user_input.lower() == "session":
                    self.cmd_session()
                    continue
                
                elif user_input.lower() == "search":
                    self.cmd_search()
                    continue
                
                elif user_input.lower() == "export":
                    self.cmd_export_csv()
                    continue
                
                elif user_input.lower() == "reset":
                    self.cmd_reset()
                    continue
                
                elif user_input.lower() == "about":
                    self.cmd_about()
                    continue
                
                user_input_lower = user_input.lower()
                
                if user_input_lower in self.custom_responses:
                    response = self.custom_responses[user_input_lower]
                else:
                    response, _ = self.find_response(user_input)
                
                last_response = response
                
                timestamp = datetime.now().strftime("%H:%M:%S")
                self.conversation_history.append({
                    "speaker": "user",
                    "message": user_input,
                    "timestamp": timestamp
                })
                self.conversation_history.append({
                    "speaker": "bot",
                    "message": response,
                    "timestamp": timestamp
                })
                
                if self.user_name:
                    if self.user_name not in self.user_profiles:
                        self.user_profiles[self.user_name] = {}
                    self.user_profiles[self.user_name]["messages_sent"] = \
                        self.user_profiles[self.user_name].get("messages_sent", 0) + 1
                    self.user_profiles[self.user_name]["last_visited"] = \
                        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    self.save_user_data()
                
                print(f"Bot: {response}\n")
            
            except KeyboardInterrupt:
                print("\n\nBot: Interrupted! Saving conversation...")
                self.cmd_save_conversation()
                print("Bot: Goodbye!")
                break
            
            except Exception as e:
                print(f"Bot: Oops! An error occurred: {e}\n")


def main():
    chatbot = Chatbot()
    chatbot.run()


if __name__ == "__main__":
    main()
