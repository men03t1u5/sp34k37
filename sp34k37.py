import os
import sys





print "\n\n\n\n\n\n"
print r"""
		    .Lo''''''''''$$$$be.
                   -"           ^""**$$$e.
                 ."                   '$$$c
                /                      "4$$b
               d  3                      $$$$
               $  *                   .$$$$$$
              .$  ^c           $$$$$e$$$$$$$$.
              d$L  4.         4$$$$$$$$$$$$$$b
              $$$$b ^ceeeee.  4$$ECL.F*$$$$$$$
  e$""=.      $$$$P d$$$$F $ $$$$$$$$$- $$$$$$
 z$$b. ^c     3$$$F "$$$$b   $"$$$$$$$  $$$$*"      .=""$c
4$$$$L        $$P"  "$$b   .$ $$$$$...e$$        .=  e$$$.
^*$$$$$c  %..   *c    ..    $$ 3$$$$$$$$$$eF     zP  d$$$$$
  "**$$$ec   "   %ce""    $$$  $$$$$$$$$$*    .r" =$$$$P""
        "*$b.  "c  *$e.    *** d$$$$$"L$$    .d"  e$$***"
          ^*$$c ^$c $$$      4J$$$$$% $$$ .e*".eeP"
             "$$$$$$"'$=e....$*$$**$cz$$" "..d$*"
               "*$$$  *=%4.$ L L$ P3$$$F $$$P"
                  "$   "%*ebJLzb$e$$$$$b $P"
                    %..      4$$$$$$$$$$ "
                     $$$e   z$$$$$$$$$$%
                      "*$c  "$$$$$$$P"
                       .'''*$$$$$$$$bc
                    .-"    .$***$$$'''*e.
                 .-"    .e$"     "*$c  ^*b.
          .=*'''    .e$*"          "*bc  '*$e..
        .$"        .z*"               ^*$e.   '*****e.
        $$ee$c   .d"                     "*$.        3.
        ^*$E")$..$"                         *   .ee==d%
           $.d$$$*                           *  J$$$e*
            '''                              "$$$"
"""
print "\t\t\tSP34K37"
print
print "\t\tCause every shell needs a voice!\n\n"
print
print "Dependencies: sudo apt-get install mpg123"
print 
print
print "Usage: python sp34K37.py"
print "Author: MEN03T1U$"
print "Brought to you by: NAHC"

try:

	while True:


		choice = int(raw_input('\nWhat Language?\n\n\nEnglish - 1\nPortuguese - 2\nSpanish - 3\n\n\n----CTRL-C to quit ----->' ))

		if choice == 1 :
				host = raw_input('\nHacker says what?\n>')

		

				response = os.system(' googlesay(){ curl -s -A RG translate\.google\.com/translate_tts -d "tl=en&q=$*" |mpg123 -q -; }; googlesay ' + host)
		
		elif choice == 2:
				host = raw_input('\nHacker says what?\n>')



				response = os.system(' googlesay(){ curl -s -A RG translate\.google\.com/translate_tts -d "tl=pt&q=$*" |mpg123 -q -; }; googlesay ' + host)
		elif choice == 3:
				host = raw_input('\nHacker says what?\n>')

			

				response = os.system(' googlesay(){ curl -s -A RG translate\.google\.com/translate_tts -d "tl=es&q=$*" |mpg123 -q -; }; googlesay ' + host)
		
		else:
				print "error"
				sys.exit(0)

except KeyboardInterrupt:
	print "\nHasta la vista, baby!\n"
	response = os.system(' googlesay(){ curl -s -A RG translate\.google\.com/translate_tts -d "tl=es&q=$*" |mpg123 -q -; }; googlesay ' + 'Hasta la vista. baby')
	sys.exit(0)
