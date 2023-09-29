public class RotationCalculator {
    
    public void addRotation(Vector3f axis, Angle rotation) {
        Quaternion q = new Quaternion(rotation, axis);
        Matrix result = new Matrix(4, 4);
        Matrix quaternion = q.getRotationMatrix();

        Matrix.multiply(matrix, q.getRotationMatrix(), result);
        matrix = result;
    }
}