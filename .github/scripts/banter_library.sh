#!/bin/bash
# .github/scripts/banter_library.sh
# Centralized banter message and reaction library

declare -A BANTER_MODES=(
  [british]="🇬🇧"
  [pirate]="🏴‍☠️"
  [cockney]="🐭"
  [upper-class]="👑"
  [yorkshire]="⚪"
  [scottish]="🏰"
  [posh-london]="💍"
)

# ============================================================
# Commit Messages Library
# ============================================================

get_british_messages() {
  cat <<'EOF'
fix: squashed that bug like a proper legend 💂🛠️🔥
feat: added a cheeky new feature, sorted innit bruv 🧃✨💂
chore: tidied up the config, all neat now 🔥🧃🧹
docs: wrote it all down like a true gent 💂📚🧃
refactor: cleaned up the mess, proper tidy 🔧💂🧃
style: made it look snazzy, innit 🎨🧃💂
test: gave it a proper poke, all green now ✅💂🧃
fix: patched it up like a boss 🔥🛠️💂
feat: dropped a spicy new bit of code 🌶️💂🧃
chore: decluttered the codebase, lovely jubbly 🧽💂✨
perf: made it faster than a London underground 🚇⚡💂
fix: ironed out the wrinkles, looking sharp 👔🔧💂
feat: brilliant innovation, that is 💡🧃✨
docs: documented it better than the Queen's English 👑📖💂
refactor: restructured the whole thing, Bob's your uncle 🎯💂
test: tested it within an inch of its life ✅🔬💂
EOF
}

get_pirate_messages() {
  cat <<'EOF'
fix: arrr, slayed that bug like a fearless buccaneer 🏴‍☠️⚔️💀
feat: shiver me timbers, added treasure of a feature 🏴‍☠️💎✨
chore: swab the deck, cleaned up this code proper like 🧹⚓🏴‍☠️
docs: wrote it down like a captain's log, it is 📜🏴‍☠️⚓
refactor: plundered and pillaged the codebase, savvy 🗺️💀✨
style: polished like a pirate's cutlass, it be shinin' 🗡️✨🏴‍☠️
test: tested with the wrath of Davy Jones himself ⚓💀✅
fix: fixed it faster than ye can say 'yo ho ho' 🏴‍☠️⚡💂
feat: dropped a booty load of new code, matey 🏴‍☠️💰🧃
chore: cast off the barnacles, ship be fresh now 🚢✨💀
perf: sped it up like a pirate ship in a hurricane 🌪️⚓⚡
fix: patched the hull breach with cannons of code 🏴‍☠️🔫💎
feat: a legendary new feature, tell all the seven seas 🌊🏴‍☠️💡
docs: scrolled the knowledge like an old treasure map 🗺️📖🏴‍☠️
refactor: reorganized like a pirate's plundered fortress 🏴‍☠️🎯💀
test: gave it the trials of the Caribbean, it survives 🌊✅⚓
EOF
}

get_cockney_messages() {
  cat <<'EOF'
fix: blimey, fixed that bug innit, ain't it sweet 💪🐢✨
feat: cor strike a light, got a new feature for ya gal 🌟✨👑
chore: tidy up the gaff, clean as a whistle now mate 🧹✨🎩
docs: wrote it all down proper, like a London geezer 📖🎩✨
refactor: rearranged the crib, all spick and span bruv 🎯💪🎩
style: made it look lush, innit a beaut 🎨✨💚
test: poked it about somethin' fierce, all sorted yeah 🔍✅💪
fix: done it up like a proper cockney warrior, no sweat 🐭⚔️✨
feat: blimey, dropped some mint new bits of code 🌿💚✨
chore: swept out the old, brought in the new, lovely 🧹💚🎩
perf: made it quicker than a London cabbie, nuff said ⚡🚕💚
fix: patched it up slicker than ye old codger's pipe 🔧✨🎩
feat: stone the crows, this feature is the bees knees 🐝👑💚
docs: scribbled it down like old Dick Whittington 📜🎩✨
refactor: reorganized like a proper market stall arrangement 🎯💪🏪
test: gave it a right old going over, bob's yer uncle ✅🐭🎩
EOF
}

get_upper_class_messages() {
  cat <<'EOF'
fix: one has quite efficiently eliminated the offending bug, what what 🎩👑✨
feat: a most splendid feature has been introduced to one's codebase, naturally 💎🥂✨
chore: the repository has been organised with the utmost propriety, I assure you 🧹👑✨
docs: documentation crafted with the precision of Oxford scholars, indeed 📚👑🎩
refactor: the code structure has been restructured with aristocratic elegance 🎯💎✨
style: the aesthetics have been refined to the highest standards of sophistication 🎨👑💎
test: one has subjected the code to rigorous examination, most thoroughly 🔬✅👑
fix: the malfunction has been rectified with the grace of a Mayfair gentleman 🎩✨💎
feat: a magnificent contribution to the digital estate, positively splendid 💡👑🥂
chore: the digital manor has been tidied to perfection, indubitably so 🧹✨👑
perf: acceleration achieved with the finesse of a Rolls-Royce engine ⚡🚗💎
fix: patched with the precision of a Savile Row tailor, exceedingly fine 🔧👑✨
feat: a most distinguished innovation for the discerning programmer, I say 💎🎩✨
docs: documented with the eloquence of a Cambridge Don, supremely executed 📖👑🎩
refactor: restructured with the deportment of Windsor Castle guardians 🏰💎👑
test: examined with the rigour of a Buckingham Palace inspection, absolutely flawless ✅👑💎
EOF
}

get_yorkshire_messages() {
  cat <<'EOF'
fix: right then, fixed that bug like a proper Yorkshire warrior 🛠️💪⚪
feat: nay bother, added a grand feature, none of yer nonsense 💡✨⚪
chore: sorted the codebase, clean as a new cloth on t'loom 🧹⚪✨
docs: wrote it all down proper, like a true Yorkshire scribe 📖⚪💪
refactor: reorganized t'whole thing, neat and tidy like 🎯⚪💪
style: made it look right grand, that code does 🎨✨⚪
test: poked at it till it squealed, all working now 🔍✅⚪
fix: fixed it faster than you can say 'eh bab' 🏃⚡⚪
feat: by 'eck, added some cracking new code, proper champion 🏆✨⚪
chore: cleaned up t'mess, neat and proper like 🧹💪⚪
perf: sped up faster than a Yorkshire pudding in t'oven ⚡🍲⚪
fix: patched it up like a proper Yorkshire tradesman 🔧⚪💪
feat: this feature's a real belter, I tell thee 💎✨⚪
docs: documented it better than t'Leeds Library, I reckon 📚⚪💪
refactor: restructured like a Yorkshire stone wall, solid as owt ⛏️⚪💪
test: tested it within an inch of its life, Yorkshire style ✅⚪💪
EOF
}

get_scottish_messages() {
  cat <<'EOF'
fix: och aye, bashed that bug like a true Scot 🥃⚔️🍺
feat: bonnie wee feature, aye ye dinnae get better than this 💡✨🏰
chore: tidied up the codebase, clean as a highland loch 🧹✨🏔️
docs: wrote it doon like a true son o' Scotland 📖🏰⚔️
refactor: reorganized tae perfection, as they dae in Edinburgh 🎯✨🏰
style: made it bonnie tae look upon, a true Caledonian marvel 🎨🏰✨
test: tested it tougher than Highland heather, all sorted 🔍✅🏔️
fix: fixed faster than a Speyside distillery works its magic ⚡🥃✨
feat: a bonnie new feature, aye the best in a' the land 💎🏰🥃
chore: swept oot the auld, brought in the new, braw 🧹🏰✨
perf: sped up like Loch Ness waters in flood, I tell ye 🌊⚡🏔️
fix: patched it like a true Scottish craftsman, nae messin' 🔧🏰💪
feat: this feature's a bonnie doozy, straight frae the Highlands 🏔️💡🥃
docs: documented it better than Robert Burns himself 📖⚔️🏰
refactor: reorganized like a proper Scottish fortification, solid 🏰🎯💪
test: tested it tae the limits, och ye beauty 🔬✅🥃
EOF
}

get_posh_london_messages() {
  cat <<'EOF'
fix: frightfully good show, vanquished that pesky bug from Chelsea 🎩💎✨
feat: darling, we've procured a most delightful feature for SW1A 1AA 💎🎩✨
chore: the codebase has been organised with the panache of Belgravia finest 🧹👑✨
docs: documented with the eloquence of a Knightsbridge scholar, naturally 📚💎🎩
refactor: restructured with the finesse of a Kensington townhouse restoration 🏘️✨💎
style: polished to the lustrous gleam of polished Knightsbridge marble 🎨💍✨
test: subjected to the rigorous standards of a Mayfair investment review ✅👑💎
fix: rectified with the precision of a Bespoke Savile Row tailor 🔧🎩✨
feat: an absolutely divine contribution, worthy of The Ritz itself 💡👑🥂
chore: organised with the meticulousness of a Claridge's concierge 🧹✨💍
perf: accelerated with the smoothness of a Bentley on Park Lane ⚡🚗💎
fix: patched with the elegance of a Harrods fine restoration service 🔧💍✨
feat: a positively exquisite innovation, strictly for the discerning coder 💎👑✨
docs: composed with the sophistication of a Claridge's invitation, I must say 📖🎩💍
refactor: restructured with the architectual grandeur of Westminster Abbey 🏰💎👑
test: examined with the meticulous care of a Sotheby's appraisal, absolutely impeccable ✅💍👑
EOF
}

# ============================================================
# Reaction Comments Library
# ============================================================

get_british_reactions() {
  cat <<'EOF'
Nice one, bruv! — commit %COMMIT% is looking mint 💂🧃
Cor blimey! That's a belter of a commit, that is 🚀💂
Sorted! Commit %COMMIT% is absolutely pukka 👑✨
Blimey, you've done well there! Absolute cracker 💪💂
Top marks! Commit %COMMIT% is the bee's knees 🐝💂
Brilliant work, mate! That's a gem of a commit 💎🧃
EOF
}

get_pirate_reactions() {
  cat <<'EOF'
Shiver me timbers! Commit %COMMIT% be fit for the high seas 🏴‍☠️💎
Arrr, ye be a true buccaneer! That commit be legendary 🏴‍☠️⚔️
Yo ho ho! Commit %COMMIT% be worth its weight in doubloons 🏴‍☠️💰
Blimey, ye've plundered a fine piece of code there, matey! 🏴‍☠️✨
Dead men tell no tales, but this commit %COMMIT% speaks volumes! 🏴‍☠️💀
Avast ye! That be the finest work ever to sail these digital seas 🏴‍☠️🌊
EOF
}

get_cockney_reactions() {
  cat <<'EOF'
Blimey! Commit %COMMIT% is the dog's dinner, innit! 🐭✨
Stone the crows, that's a belter mate! Proper lush work 💚👑
Cor strike a light! Ye did good there gal, real good 🌟💪
Blimey, I ain't never seen code so clean, lovely jubbly! 🧹✨
Stone my crows, commit %COMMIT% is mint innit, top drawer! 💚🎩
Aw nah fam, that code be fresher than a Billingsgate catch! 🐟✨
EOF
}

get_upper_class_reactions() {
  cat <<'EOF'
Most extraordinary! Commit %COMMIT% exemplifies the pinnacle of elegance 👑💎
One must congratulate you forthwith—this is positively Shakespearean coding! 🎭👑
Absolutely smashing! A commit of such refinement rarely graces our repositories 💎✨
Pip pip! Commit %COMMIT% is fit for Her Majesty's personal collection 👑🏰
Indubitably magnificent! The workmanship here is simply beyond reproach 🎩💎
What ho! This code exhibits the sophistication of a well-tailored waistcoat indeed! 👔✨
EOF
}

get_yorkshire_reactions() {
  cat <<'EOF'
By 'eck, that's a cracking commit there, mate! 💪⚪
Right then, commit %COMMIT% is nay bother, proper champion stuff 🏆⚪
Eh up, that code's grand as owt! Braw work, duck 💡✨
Stone the crows, that commit's a real belter innit! 🎯⚪
Nay nonsense, that's quality work, proper Yorkshire pride 💪⚪
By gum, ye've done summat special there, real proper like! ✨⚪
EOF
}

get_scottish_reactions() {
  cat <<'EOF'
Och aye, that commit's bonnie as a Highland morning! 🏰💎
By the waters o' Loch Ness! Commit %COMMIT% is absolutely braw! 🌊✨
Aye, that's the finest work I've seen oot o' the Lowlands! 🏰🥃
Och, ye're a true son o' Scotland with that code! 💪🏔️
Blimey, that commit's worth a dram o' the finest whisky! 🥃✨
Haud yer wheesht, that's pure dead brilliant, mate! 🎯⚔️
EOF
}

get_posh_london_reactions() {
  cat <<'EOF'
Absolutely divine! Commit %COMMIT% is fit for The Ritz itself, darling 👑💍
Frightfully good show! One's impressed with such Knightsbridge-calibre work 🏘️💎
Pip pip! That commit would grace any Mayfair establishment, truly exquisite 🎩✨
Positively smashing! Commit %COMMIT% is the epitome of Chelsea elegance 💎👑
I say, what a splendid piece of work from a Belgravia perspective! 👔✨
Absolutely posh! This commit's worthy of a Claridge's celebration, old sport 🥂💍
EOF
}

# ============================================================
# Main Functions
# ============================================================

get_banter_message() {
  local mode="$1"
  local messages
  
  case "$mode" in
    pirate) messages=$(get_pirate_messages) ;;
    cockney) messages=$(get_cockney_messages) ;;
    upper-class) messages=$(get_upper_class_messages) ;;
    yorkshire) messages=$(get_yorkshire_messages) ;;
    scottish) messages=$(get_scottish_messages) ;;
    posh-london) messages=$(get_posh_london_messages) ;;
    *) messages=$(get_british_messages) ;;
  esac
  
  # Select random message
  echo "$messages" | shuf -n 1
}

get_reaction_comment() {
  local mode="$1"
  local commit_sha="$2"
  local reactions
  
  case "$mode" in
    pirate) reactions=$(get_pirate_reactions) ;;
    cockney) reactions=$(get_cockney_reactions) ;;
    upper-class) reactions=$(get_upper_class_reactions) ;;
    yorkshire) reactions=$(get_yorkshire_reactions) ;;
    scottish) reactions=$(get_scottish_reactions) ;;
    posh-london) reactions=$(get_posh_london_reactions) ;;
    *) reactions=$(get_british_reactions) ;;
  esac
  
  # Select random reaction and replace commit hash
  local comment=$(echo "$reactions" | shuf -n 1)
  echo "${comment//%COMMIT%/$commit_sha}"
}

# Export functions for use in workflow
export -f get_banter_message
export -f get_reaction_comment
