import pygame

class Stage:
    def __init__(self, GM):
        print("Stage init")
        self.stage = self.get_stage(GM)
        self.stage.run()

    def get_stage(self, GM):
        if GM.stageIdx == 0:
            from stages.stage0 import Stage0
            return Stage0(GM)
        elif GM.stageIdx == 1:
            from stages.stage1 import Stage1
            return Stage1(GM)
        elif GM.stageIdx == 2:
            from stages.stage2 import Stage2
            return Stage2(GM)
        else:
            raise ValueError(f"Invalid stage number: {GM.stageIdx}")
