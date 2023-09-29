public class MidiUpdater {
    private Synthesizer synthesizer;

    public MidiUpdater(Synthesizer synth) {
        this.synthesizer = synth;
    }

    private void updateGain() {
        int pos = getValue();
        int value = (int) ( 127 * ( double ) ( pos / 100.0 ));
        MidiChannel[] cs = synthesizer.getChannels();

        for( int I = 0; I < cs.length; i++ ) {
            cs[ i ].controlChange( 7, value );
        }
    }
}