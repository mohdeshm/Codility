package codility;

import java.util.ArrayList;
import java.util.List;

public class PbSt1 {

	int pit;
	int j = 0;
	int i = 0;
	ArrayList<Integer> ps = new ArrayList<>();
	ArrayList<Integer> ns = new ArrayList<>();

	int pSum;
	int nSum;
	int min;

	public int pit(int[] A) {
		int length = A.length;
		while (j < length - 1) {

			if (A[j] == A[j + 1]) {
				j++;
				continue;
			}
			while (j < length - 1 && A[j] > A[j + 1]) {

				pSum += (A[j] - A[j + 1]);
				j++;
			}

			if (pSum != 0) {
				ps.add(pSum);
				pSum = 0;

				while (j < length - 1 && A[j] < A[j + 1]) {
					nSum += (A[j + 1] - A[j]);
					j++;
				}
			} else {
				j++;
			}
			if (nSum != 0) {
				ns.add(nSum);
				nSum = 0;
			}

		}
		int size = ns.size();
		for (int i = 0; i < size; i++) {
			if (ps.get(i) <= ns.get(i)) {
				min = ps.get(i);
			} else {
				min = ns.get(i);
			}
			if (pit < min) {
				pit = min;
			}
		}
		return pit;

	}

	public static void main(String[] args) {
		PbSt1 pits = new PbSt1();
		int[] A = { 0, 1, 3, -2, 0, 3, 0, -3, 2, 3};
		int answer=pits.pit(A);
		System.out.println(answer);
	}

}
