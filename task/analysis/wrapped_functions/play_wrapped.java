public class Simulator {
    public void play(){
        if( currentState == SimulatorState.STOPPED ){
            setSimulationTime( 0 );
            simItem.initialize();
            startTimer();
            setState( SimulatorState.PLAYING );
        }
        else if( currentState == SimulatorState.PAUSED ){
            startTimer();
            setState( SimulatorState.PLAYING );
        }
    }
}