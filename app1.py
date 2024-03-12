import pyglet as pg

window = pg.window.Window()

label = pg.text.Label('Hello, world',
                      font_name='Times New Roman',
                      font_size=36,
                      x=window.width//2, y=window.height//2,
                      anchor_x='center', anchor_y='center')

batch = pg.graphics.Batch()

star1 = pg.shapes.Star(800, 400, 60, 60, num_spikes=3, color=(255, 255, 0), batch=batch)
star2 = pg.shapes.Star(800, 200, 60, 1, num_spikes=3, color=(255, 255, 0), batch=batch)
star3 = pg.shapes.Star(400, 200, 60, -60, num_spikes=3, color=(255, 255, 0), batch=batch)
star4 = pg.shapes.Star(400, 400, 60, -60, num_spikes=6, color=(255, 255, 0), batch=batch)
star5 = pg.shapes.Star(200, 400, 60, -10, num_spikes=3, color=(255, 255, 0), batch=batch)


@window.event
def on_draw():
    window.clear()
    label.draw()
    batch.draw()


if __name__ == '__main__':
    pg.app.run()
