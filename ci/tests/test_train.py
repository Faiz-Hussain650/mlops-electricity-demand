from ml.train import load_and_preprocess

def test_data_load():
    df = load_and_preprocess("data/household_power.txt")
    assert not df.empty
    assert "Global_active_power" in df.columns
