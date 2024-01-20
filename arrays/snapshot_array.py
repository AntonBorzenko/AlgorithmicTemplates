import bisect


class SnapshotArray:

    def __init__(self, length: int):
        self.arrays = [[[0, 0]] for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        if self.arrays[index][-1][0] == self.snap_id:
            self.arrays[index][-1][1] = val
        else:
            self.arrays[index].append([self.snap_id, val])

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def set_snap_id(self, snap_id: int):
        if snap_id < self.snap_id:
            raise ValueError(f'snap_id should be at least {self.snap_id}')
        self.snap_id = snap_id

    def get(self, index: int, snap_id: int | None = None) -> int:
        if snap_id is None:
            snap_id = self.snap_id
        arr = self.arrays[index]
        idx = bisect.bisect_left(arr, [snap_id, -1])

        if idx == len(arr) or arr[idx][0] > snap_id:
            return arr[idx - 1][1]

        return arr[idx][1]
