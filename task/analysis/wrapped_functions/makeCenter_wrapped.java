public class CenterMaker {
    public Component makeCenter() {
        JPanel imageCanvas = new JPanel();
        imageCanvas.addMouseListener( new MouseAdapter() {
            @SuppressWarnings( "synthetic-access" )
            @Override
            public void mouseClicked( MouseEvent e ) {
                actionImageMouse( e );
            }
        });

        imageCanvas.add( new JLabel( new ImageIcon( SWGFrame.class.getResource( "images/swg.png" ))));

        return new JScrollPane( imageCanvas );
    }

    private void actionImageMouse( MouseEvent e ) {
        // implementation details
    }
}