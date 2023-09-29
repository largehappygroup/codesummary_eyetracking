public class WordFormGeneratorParser {

    public WordFormGenerator getFastestGenerator( final Locale locale ) throws MorphologyException {
        if ( locale == null ) {
            throw new IllegalArgumentException( "The 'loc' argument cannot be null." );
        }
        WordFormGenerator component = ( WordFormGenerator ) fastestGenerators.get( locale );
        if ( component == null ) {
            throw new MorphologyException( "Cannot find generator for locales : " + locale.toString() );
        }
        return component;
    }

}