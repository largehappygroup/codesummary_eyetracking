public class MyClass {
    private void leaveAll( MouseEvent<? extends EventHandler > event ) {
        LocInfo locInfo = new LocInfo();
        assert( !locInfo.isVertexLocValid() );
        assert( !locInfo.isVerticalEdgeLocValid() );
        assert( !locInfo.isHorizontalEdgeLocValid() );
        assert( !locInfo.isCellLocValid() );
        handleLeaveEvents( locInfo, event );
        lastLocInfo.copy( locInfo );
    }
}