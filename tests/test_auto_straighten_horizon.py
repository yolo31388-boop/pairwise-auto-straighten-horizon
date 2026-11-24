import pytest
import imaging.auto_straighten_horizon as mod

CASES = [
    ("angle_full_res", (1,)),
    ("crop_by_content", (1,)),
    ("kernel_by_angle", (1,)),
    ("shared_baseline", (1,)),
    ("exclude_reflection", (1,)),
    ("post_check", (1,)),
    ("load", (1,)),
    ("detect", (1,)),
    ("straighten", (1,)),
    ("export", (1,)),
    ("validate_straighten", (1,)),
    ("metrics", (1,)),
    ("audit", (1,)),
    ("fallback", (1,)),
    ("determinism", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
