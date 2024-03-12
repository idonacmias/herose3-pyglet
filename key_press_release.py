import pyglet as pg


class M(pg.window.Window):
    def on_key_press(self, symbol, modifiers):
        print(f'A key was pressed, {chr(symbol)}')

    def on_key_release(self, symbol, modifiers):
        print(f'A key was released, {chr(symbol)}')


if __name__ == '__main__':
    window = M()
    pg.app.run()
