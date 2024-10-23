class PositionManager:
    def __init__(self):
        self.positions = {}  # {file_id: position(float)}

    def set_position(self, file_id: str, position: float):
        self.positions[file_id] = position

    def get_position(self, file_id: str) -> float:
        return self.positions.get(file_id, 0)

    def remove_position(self, file_id: str):
        if file_id in self.positions:
            del self.positions[file_id]

    def get_all_positions(self) -> dict:
        return self.positions

    def reset(self):
        self.positions = {}


position_manager = PositionManager()
