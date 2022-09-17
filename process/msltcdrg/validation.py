def validate_drg_dataframe(df) -> bool:
    """Validate that a DRG DataFrame has the appropriate attributes"""
    dtypes = {"drg": int, "relative_weight": float, "gmlos": float, "sso": float}
    for field, dtype in dtypes.items():
        assert df.dtypes[field] == dtype

    # First DRG is 1
    assert df.iloc[0, 0] == 1

    # Last DRG is 999
    assert df.iloc[-1, 0] == 999

    return True
