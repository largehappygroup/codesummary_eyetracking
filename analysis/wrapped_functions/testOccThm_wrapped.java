public class OccThmTester {
    public void testOccThm() throws Exception {
        final IContextRoot context = ResourceUtils.createContext( rodinProject, CTX_BARE_NAME, CST_1DECL_1REF_THM );
        final IConstant cst1 = context.getConstant( INTERNAL_ELEMENT1 );
        final IDeclaration declCst1 = newDecl( cst1, CST1 );
        final IAxiom thm = context.getAxiom( INTERNAL_ELEMENT1 );
        final IOccurrence occRef = makeRefPred( thm, 9, 13, declCst1 );
        final BridgeStub tk = new BridgeStub( context );
        final ContextIndexer indexer = new ContextIndexer();

        assertTrue( indexer.index( tk ));

        tk.assertOccurrencesOtherThanDecl( cst1, occRef );
    }
}