#!/bin/bash
# .github/scripts/banter_library.sh

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
fix: patched the hull breach with cannons of code 🏴‍☠️🔫💎
feat: a legendary new feature, tell all the seven seas 🌊🏴‍☠️💡
chore: cast off the barnacles, ship be fresh now 🚢✨💀
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
chore: stone the crows, swept out the old proper like 🧹💚🎩
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
Proper job! Commit %COMMIT% is as solid as they come 🔨💂
Oi oi! That's some tidy work right there, innit 🧹✨
Bob's your uncle! Commit %COMMIT% came out a treat 🎉💂
Smashing stuff! You've outdone yourself this time, bruv 🏆🧃
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
By Davy Jones! Commit %COMMIT% be a treasure beyond measure 🏴‍☠️💎
Hoist the colours! That code be worthy of the Jolly Roger 🏴‍☠️⚡
Walk the plank? Never! Commit %COMMIT% earns ye a place in me crew 🏴‍☠️⚓
Splice the mainbrace! That be some legendary code, savvy 🏴‍☠️🥃
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
Gawd blimey! Commit %COMMIT% is pure gold, no messin' 💛🐭
Right result that is! You smashed it proper, me old china 🎯✨
Cor love a duck! Commit %COMMIT% is the real McCoy 💚👑
Knees up! That code is cleaner than a new pair of plates 🦶✨
EOF
}

get_upper_class_reactions() {
  cat <<'EOF'
Most extraordinary! Commit %COMMIT% exemplifies the pinnacle of elegance 👑💎
One must congratulate you forthwith — this is positively Shakespearean coding! 🎭👑
Absolutely smashing! A commit of such refinement rarely graces our repositories 💎✨
Pip pip! Commit %COMMIT% is fit for Her Majesty's personal collection 👑🏰
Indubitably magnificent! The workmanship here is simply beyond reproach 🎩💎
What ho! This code exhibits the sophistication of a well-tailored waistcoat indeed! 👔✨
I say! Commit %COMMIT% is the finest contribution since the Magna Carta 📜👑
Bravo! One hasn't seen such elegant code since one's days at Eton 🎓💎
Frightfully good! Commit %COMMIT% deserves a mention in Debrett's 📖👑
By Jove! That code is as impeccable as a Savile Row suit 🎩✨
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
Eee by gum! Commit %COMMIT% is worth its weight in Yorkshire pudding 🍲⚪
Champion work that is! Tha's done thi'sen proud today 🏆💪
Now then! Commit %COMMIT% is as solid as a dry stone wall ⛏️⚪
Reight good that is! Tha knows how to write code proper like 💡⚪
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
By the bonnie banks! That code's finer than a Highland reel 🎵🏔️
Hoots mon! Commit %COMMIT% is worthy of a Highland fling 💃🥃
Awa' wi' ye! That's the bonniest code I've seen a' week 🏰💎
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
My word! Commit %COMMIT% is as refined as a Fortnum & Mason hamper 🧺💎
Topping stuff! That code belongs in the National Gallery, darling 🎨👑
Rather! Commit %COMMIT% is the talk of the Garrick Club tonight 🎭💍
Spiffing work! One would expect nothing less from such a distinguished coder 🎩✨
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

  local comment=$(echo "$reactions" | shuf -n 1)
  echo "${comment//%COMMIT%/$commit_sha}"
}

export -f get_banter_message
export -f get_reaction_comment
