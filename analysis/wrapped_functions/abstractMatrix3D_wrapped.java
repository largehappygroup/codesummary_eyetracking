public class Matrix3D extends AbstractMatrix3D {
    
    protected AbstractMatrix3D vDice(int axis0, int axis1, int axis2) {
        super.vDice(axis0, axis1, axis2);

        // swap offsets
        int[][] offsets = new int[3][];
        offsets[0] = this.sliceOffsets;
        offsets[1] = this.rowOffsets;
        offsets[2] = this.columnOffsets;

        this.sliceOffsets = offsets[axis0];
        this.rowOffsets = offsets[axis1];
        this.columnOffsets = offsets[axis2];

        return this;
    }
}