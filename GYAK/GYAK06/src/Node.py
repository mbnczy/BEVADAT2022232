class Node:
    def __init__(
        self,
        feature_index=None,
        threshold=None,
        left=None,
        right=None,
        value=None,
        info_gain=None,
    ) -> None:
        # leaf
        self.value = value

        # dis
        self.feature_index = feature_index
        self.threshold = threshold
        self.right = right
        self.left = left
        self.info_gain = info_gain
