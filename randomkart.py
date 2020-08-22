import tracery
from tracery.modifiers import base_english


race_locations = {
  'origin': '#planet.a#',
  'planet-prefix': ['vibrant', 'small', 'desert', 'ice', 'fire', 'forbidden', 'dominion-controlled', 'mining', 'uninhabited', 'large'],
  'planet-suffix': ['with no atmosphere', 'full of wildlife', 'with hostile alien life', 'with #amusement-park-description.a# amusement park', 'with extreme gravity', 'with low gravity', 'with an ancient secret', 'with bad reception', 'with large canyons', 'with #weather-description# weather', 'controlled by #syndicate-description.a# syndicate'],
  'planet': ['#planet-prefix# planet with #course-description#','planet #planet-suffix#', '#satellite-prefix# satellite', 'satellite #satellite-suffix#'],
  'satellite-prefix': ['small', 'wildly-spinning', 'pirate', 'huge', 'industrial', 'mysteriously empty', 'luxory', 'entertainment', 'well-made', 'ancient', 'dominion-controlled'],
  'satellite-suffix': ['controlled by a #ai-personality# AI', 'with no power', 'with frequent blackouts', 'with hostile robotic workers', 'with low gravity', 'with extreme gravity', 'made of glass', 'with bad reception', 'with tight corridors', 'with frequently changing holograms', 'with inverted gravity', 'owned by #syndicate-description.a# syndicate' ],
  'course-description': ['no judges', 'tiered bridges', 'active volcanoes', 'kaiju-style monsters', 'many conveyor belts', 'randomly changing architecture', 'heavy traffic' ],
  'ai-personality': ['sadistic', 'benevolent', 'absent-minded', 'sketchy', 'inquisative', 'malfunctioning', 'charming'],
  'amusement-park-description': ['beloved', 'haunted', 'run-down', 'technologically advanced', 'ancient'],
  'weather-description': ['erratic', 'gloomy', 'forboding', 'dangerous', 'sunny', 'torrential'],
  'syndicate-description': ['notorious', 'benevloent', 'ruthless', 'roguish', 'wealthy', 'friendly']
}

bike_events = {
    'origin': '#event#', 
    'event': ['#enemy.a# attacks you', 'a swarm of #[plural:s]alien# surround you', 'you are ambushed by #enemy.a#', 'you encounter #disaster-prefix.a# #disaster#', 'you must navigate around #disaster-prefix.a# #disaster#', '#enemy.a# attempts to #bike-part-attack# your #bike-part#', 'your #bike-part# #bike-part-accident#', 'you are challenged to a duel by #racer.a#', 'you are blind-sided by #enemy.a#', '#racer.a# attempts to #player-accident#', '#racer.a# activates #racer-ability.a# and takes the lead', '#racer.a# teams up with #racer.a# to #player-accident#', '#racer.a# trains #[plural:]alien.a# to #player-accident#', 'your bike #bike-accident#'],
    'enemy': ['swarm of #[plural:s]alien#', '#alien-adjective# #[plural:]alien#', '#racer#'],
    'racer': ['#person-adjective# #racer-type# #appearance#', 'xeno #mutation-suffix#', '#racer-type# wearing #color.a# #clothing#'],
    'racer-type': ['dude', 'lady', 'man', 'xeno'],
    'racer-ability': ['speed boost', 'rocket jump', 'hook shot', 'tunneling device'],
    'person-adjective': ['young','big', 'small', 'unhinged', 'twitchy', 'psychotic', 'neurotic', 'roguish', 'drunken', 'psychic', 'possessed', 'nervous', 'jacked', 'classically handsome', 'dapper', 'bored-looking', 'live-streaming'],
    'appearance': ['wearing #color#', 'dressed from head to toe in #clothing-material#', 'in #armor-adjective# armor'],
    'color': ['red', 'yellow', 'black', 'blue', 'gold', 'silver', 'green', 'purple', 'organge'],
    'armor-adjective': ['leather', 'plasteel', 'holographic', 'nano-swarm'],
    'clothing-material': ['denim', 'spandex', 'nanofiber', 'gold', 'velvet', 'satin', 'lace', 'terrycloth', 'polyester', 'tulle'],
    'clothing': ['disco jumpsuit', 'dress', 'tuxedo', 'banana hammock',  'ball cap', 'skirt', 'cowboy hat', 'rollerblades', 'unitard', 'full-body suit', 'infinity scarf', 'samurai mask', 'gas mask', 'fingerless glove', 'driving glove', 'space suit', 'biohazard suit'],
    'disaster': ['hurricane', 'wildfire', 'tornado', 'earthquake', 'flood', 'lightning storm', 'mudslide', 'crater', 'mountain', 'force-field', 'automated turret', 'attack drone'],
    'disaster-prefix': ['sudden', 'large', 'artifically-generated', 'unusual', 'temporally-unstable', 'unavoidable'],
    'alien': ['#animal#-#animal# hybrid#plural#', '#mutation-prefix# #animal##plural#', '#animal##plural# #mutation-suffix#'],
    'alien-adjective': ['dangerous', 'aggressive', 'sleepy', 'cranky', 'shy'],
    'animal': ['deer', 'wolf', 'raccoon', 'crab', 'kangaroo', 'weasel', 'cat', 'gopher', 'spider', 'bat', 'ape', 'chipmunk', 'elephant', 'giraffe', 'capybara', 'walrus'],
    'mutation-suffix': ['with two heads', '', 'with crab claws', 'with a creepy aura', 'with the head of #animal.a#', 'that can fly', 'with poisonous spikes', 'made of pure energy', 'made of gas', 'with #number# tails', 'made of goo', 'that won\'t stop panting', 'made of needles', 'with #number# eye stalks'],
    'mutation-prefix': ['giant', 'radioactive', 'astral-projecting', 'inside-out', 'robotic' , 'hyper-intelligent', 'lighning-fast', 'super fuzzy', 'semi-transparent', 'large-eyed', 'tiny', 'baby', 'bony', 'insect-like', 'hairy', 'smooth'],
    'number': ['3','5','9','12'],
    'bike-part-attack': ['disable', 'overcharge', 'dismount', 'shoot'],
    'bike-part-accident': ['explodes', 'fizzles out with a puff of smoke', 'discharges suddenly', 'gets stuck in activation mode', 'won\'t activate'],
    'bike-accident':['gets stuck in goo', 'gets stuck in a time loop', 'gets hit by lightning', 'runs out of juice', 'starts overheating', 'starts vibrating irratically', 'is hacked by #racer.a#'],
    'bike-part': ['engines system', 'steering system', 'navigation unit', '#left-right# thruster', 'comms device', 'brake system', 'weapons system'],
    'left-right': ['left', 'right'],
    'player-accident': ['knock #player# off the bike', 'charm #player#', 'attack #player# with the way', 'bribe #player#', 'humiliate #player#', 'flip your bike', 'jump onto your bike', 'steer you into #disaster-prefix.a# #disaster#', 'kamikaze you'],
    'player': ['Wade', 'Adam']
}

grammar = tracery.Grammar(race_locations)
#grammar = tracery.Grammar(bike_events)
grammar.add_modifiers(base_english)

for i in range(0,20):
  print(grammar.flatten("#origin#"))  # prints, e.g., "Hello, world!"


