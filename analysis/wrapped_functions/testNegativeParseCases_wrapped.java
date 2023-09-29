public class TestCases {
  public void testNegativeParseCases() {
    verbose( "--->Negative parse tests  START" );

    for ( int i = 0; i < negativeParseTests.length; i++ ) {
        parseFilter( negativeParseTests[ i ], false );
    }
    // This used to fail until the parser was rewritten with the stack
    // stuff so that it can clean up partially parsed expression trees.
    checkDelete();
  }
}