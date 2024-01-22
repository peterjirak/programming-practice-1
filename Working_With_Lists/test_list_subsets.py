from list_subsets import subset_sums_to_zero_v1
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_subset_sums_to_zero_v1_test_1():
    logger.info('Execute test: test_subset_sums_to_zero_v1_test_1')
    integer_list = [-48, 9, 11, 23, 27, -15, 43, 58, -17, 78, -24]
    subset = subset_sums_to_zero_v1(integer_list)
    assert len(subset) > 0, "A subset with length greater than zero was returned by subset_sums_to_zero_v1 for the argument list"
    subset_total = sum(subset)
    assert subset_total  == 0, "The subset returned by subset_sums_to_zero_v1 sums to zero"
    if len(subset) <= 0 or subset_total != 0:
        logger.error("subset_sums_to_zero_v1 did not find a subset of the argument list that sums to zero")
    else:
        logger.info(f"{' + '.join(list(map(str, subset)))} == 0")
    logger.info('Finished executing test: test_subset_sums_to_zero_v1_test_1')
