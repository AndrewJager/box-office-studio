#film constants
PRE_PRODUCTION_LENGTH = 0.25 # percent of production time that pre-production takes
FILMING_LENGTH = PRE_PRODUCTION_LENGTH + 0.50 # percent of time at which filming ends

MIN_GROSS_CUTOFF = 0.1 #amount below which a movie will be removed from theaters

MONDAY_MODIFIER = 0.45 # weekdays calculated as a percent of Sunday gross
TUESDAY_MODIFIER = 0.55
WENDSDAY_MODIFIER = 0.40
THURSDAY_MODIFIER = 0.35

#temp
STUDIO_CUT_USA = 0.50


#     rules for box office calculation
# hype = marketing(trailer and ads) and scale
# all days at the box office get modifiers based on:
#   A: all movies released (fighting for theaters and some audience)
#   B: same genre movies (calculated with the demand fields in the boxoffice table)
#
# First Friday only includes hype
# audience reception calculated by... IDK right now, probably a random number until I add ways to make and market the movie specifically
# First Saturday by critical reception (WOM hasn't gotten out yet)
# First Sunday calculated by a mix of critical and audience reception
# weekdays calcualted with simple weekday modifiers 
# Later weekends calculated as a whole based on audience reception alone, and broken up to individual days based on simple modifiers
#
# Holidays get a simple boost