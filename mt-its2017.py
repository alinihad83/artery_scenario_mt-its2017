import storyboard
import timeline


def createStories():
        # Create TtcCondition
        ttcCondition = storyboard.TtcCondition(1.5, 200)  # ttc 1.5sec | radius 200m
        speedConditonGreater = storyboard.SpeedDifferenceConditionFaster(5.55556)  # 20 km/h
        ttcSignalEffect = storyboard.SignalEffect("irc")
        speedAndTTC = storyboard.AndCondition(ttcCondition, speedConditonGreater)

        story = storyboard.Story(speedAndTTC, [ttcSignalEffect])

        # Vehicle stops at second 20
        timeToStop = storyboard.TimeCondition(timeline.seconds(40.5))
        vehicleToStop = storyboard.CarSetCondition("flow1.0")
        vehicleAndTimeToStop = storyboard.AndCondition(timeToStop, vehicleToStop)
        stopEffect = storyboard.StopEffect()

        stopStory = storyboard.Story(vehicleAndTimeToStop, [stopEffect])

        # Register Stories at the Storyboard
        board.registerStory(story)
        board.registerStory(stopStory)

        print("Stories loaded!")
