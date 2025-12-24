## Summary

Changed `SessionException` and `AgentException` attribute name from private (with underscores) to public to unify with other exception classes.

## Related Issue

Class #19

## Changes

### Modified Files

- `backend/exceptions/exceptions.py`

### Changes Details

Changed the attributes in `SectionException` and `AgentException`

## Impact

- No impact on existing exception handling code
- Maintains backend compatibilty
- Facilitates feature FastAPI error handler implementation

## Testing

- [x] Ruff lint passes
- [x] Ruff format passes
- [x] Varified exceptions are raised correctly
- [x] Varified attributes are accessible
