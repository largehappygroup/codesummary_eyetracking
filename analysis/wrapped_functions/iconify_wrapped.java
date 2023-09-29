public class IconifyFunction {
    public void iconify(final Frame frame) {
        Point loc = getIconifyLocation(frame);

        if (loc != null) {
            mouseMove(frame, loc.x, loc.y);
        }
        invokeLater(frame, new Runnable() {
            public void run() {
                frame.setState(Frame.ICONIFIED);
            }
        });
    }
}