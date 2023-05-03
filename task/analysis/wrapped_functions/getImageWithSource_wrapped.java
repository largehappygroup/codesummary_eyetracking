```
public class ImageParser {
    public WebImage getImageWithSource( String source ) {
        WebImage[] images = getImages();

        for ( int i = 0; i < images.length; i++ ) {
            if ( HttpUnitUtils.matches( source, images[ i ].getSource() )) return images[ i ];
        }
        return null;
    }
}
```