public class TestClass {
    
    public void test_10_bug2689872() throws Exception {
        E con = getGeneric().createElement( "elt" );
        getGeneric().addPredicates( con, makeSList( "A1" ), makeSList( "0/=1" ), false );
        getGeneric().save( con );
        runBuilder();
        SCE file = getGeneric().getSCElement( con );
        getGeneric().containsPredicates( file, emptyEnv, makeSList(), makeSList() );

        hasMarker( getGeneric().getPredicates( con )[ 0 ],
            EventBAttributes.PREDICATE_ATTRIBUTE,
            ParseProblem.LexerError,
            "/"
            );
    }
}