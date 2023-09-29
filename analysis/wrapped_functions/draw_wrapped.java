public class DrawingUtility {
    public void draw() {
        p4vj.cSketch.stroke( 0 );
        p4vj.cSketch.fill( 128 );
        p4vj.cSketch.rect( xPos, yPos, xSize, ySize );
        drawFPS();
        p4vj.cSketch.fill( 255 );
        p4vj.cSketch.textAlign( p.LEFT, p.BASELINE );
        p4vj.cSketch.textFont( p4vj.fontSS14, 14 );
        p4vj.cSketch.text( " :: Control FPS", xPos, yPos + ySize - 5 );
    }
}