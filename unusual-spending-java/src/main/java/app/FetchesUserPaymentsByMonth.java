package app;

import java.util.Set;

class Payment {
    Double amount;
    String category;
    String description;
}

public class FetchesUserPaymentsByMonth {

	public static  FetchesUserPaymentsByMonth getInstance() {
		return new FetchesUserPaymentsByMonth();
	}

	private FetchesUserPaymentsByMonth() {
	}

	public Set<Payment> fetch(long userId, int year, int month) {
		throw new RuntimeException("Data access will be implemented by a different team later");
	}

}
