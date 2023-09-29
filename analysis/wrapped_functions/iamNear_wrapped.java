public class ActorNearChecker {

   private boolean iamNear( Actor defender ) {
      short xDiff = ( short ) ( defender.getXpos() - getXpos() );
      short yDiff = ( short ) ( defender.getYpos() - getYpos() );

      if ( xDiff > 1 || yDiff > 1 || xDiff < -1 || yDiff < -1 ) {
          return false;
      }
      return true;
  } 
}