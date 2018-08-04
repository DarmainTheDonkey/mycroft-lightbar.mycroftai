# TODO: Add an appropriate license to your skill before publishing.  See
# the LICENSE file for more information.

# Below is the list of outside modules you'll be using in your skill.
# They might be built-in to Python, from mycroft-core or from external
# libraries.  If you use an external library, be sure to include it
# in the requirements.txt file so the library is installed properly
# when the skill gets installed later by a user.

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG

#DAS
import urllib.request
import urllib.parse

# Each skill is contained within its own class, which inherits base methods
# from the MycroftSkill class.  You extend this class as shown below.

# TODO: Change "Template" to a unique name for your skill
class LightbarSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(LightbarSkill, self).__init__(name="LightbarSkill")
        
        # Initialize working variables used within the skill.
        self.mode = 'off'


    @intent_handler(IntentBuilder("").require("Lightbar").require("Mode"))
    def handle_lightbar_intent(self, message):
        if message.data["Mode"] == "off":
            tx_data='0'
            self.mode="off"

        if message.data["Mode"] == "on":
            tx_data='1'
            self.mode="on"

        if message.data["Mode"] == "soft white":
            tx_data='2'
            self.mode="soft white mode"

        if message.data["Mode"] == "bright white":
            tx_data='3'
            self.mode="bright white mode"

        if message.data["Mode"] == "soft green":
            tx_data='4'
            self.mode="soft green mode"

        if message.data["Mode"] == "bright green":
            tx_data='5'
            self.mode="bright green mode"

        if message.data["Mode"] == "soft red":
            tx_data='6'
            self.mode="soft red mode"

        if message.data["Mode"] == "bright red":
            tx_data='7'
            self.mode="bright red mode"

        if message.data["Mode"] == "soft blue":
            tx_data='8'
            self.mode="soft blue mode"

        if message.data["Mode"] == "bright blue":
            tx_data='9'
            self.mode="bright blue mode"

        if message.data["Mode"] == "soft yellow":
            tx_data='10'
            self.mode="soft yellow mode"

        if message.data["Mode"] == "bright yellow":
            tx_data='11'
            self.mode="bright yellow mode"

        if message.data["Mode"] == "chase":
            tx_data='12'
            self.mode="chase mode"

        if message.data["Mode"] == "random":
            tx_data='13'
            self.mode="random mode"

        url = 'http://192.168.1.19'
        values = {'MANUAL' : tx_data }

        data = urllib.parse.urlencode(values)
        data = data.encode('utf-8')
        req = urllib.request.Request(url, data)
        response = urllib.request.urlopen(req) 

        self.speak_dialog("set.lightbar", data={"mode": self.mode})


    # The "stop" method defines what Mycroft does when told to stop during
    # the skill's execution. In this case, since the skill's functionality
    # is extremely simple, there is no need to override it.  If you DO
    # need to implement stop, you should return True to indicate you handled
    # it.
    #
    # def stop(self):
    #    return False

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return LightbarSkill()
