#!/usr/bin/env python3
# jenga_14.py

class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y


class BlockList:
    def __init__(self):
        self.blocks = []

    def add_block(self, x, y):
        self.blocks.append(Block(x, y))

    def move_blocks(self, delta_x, delta_y):
        for block in self.blocks:
            block.move(delta_x, delta_y)

    def get_center(self):
        num_blocks = len(self.blocks)
        center_x, center_y = 0, 0
        for block in self.blocks:
            center_x += block.x
            center_y += block.y
        center_x /= num_blocks
        center_y /= num_blocks
        return num_blocks, center_x, center_y


def main():
    block_list = BlockList()

    block_list.add_block(7.5, 1.5)
    block_list.add_block(1.5, 10.5)

    for _ in range(8):
        num_blocks, center_x, center_y = block_list.get_center()

        print(f"Blocks: {num_blocks:>5}\t"
              f"Center X: {center_x:>6.2f}\t"
              f"Center Y: {center_y:>6.2f}")

        block_list.move_blocks(3, 3)

        block_list.add_block(7.5, 1.5)
        block_list.add_block(1.5, 10.5)


if __name__ == "__main__":
    main()
