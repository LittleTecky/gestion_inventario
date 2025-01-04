from fastapi import HTTPException, status

# Excepción personalizada para recurso no encontrado
class ResourceNotFoundException(HTTPException):
    def __init__(self, detail: str = "Resource not found"):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=detail
        )

# Excepción personalizada para conflictos (por ejemplo, duplicados)
class ConflictException(HTTPException):
    def __init__(self, detail: str = "Conflict detected"):
        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail=detail
        )

# Excepción personalizada para entrada inválida
class InvalidInputException(HTTPException):
    def __init__(self, detail: str = "Invalid input"):
        super().__init__(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=detail
        )

# Excepción personalizada para acceso prohibido
class ForbiddenError(HTTPException):
    def __init__(self, detail: str = "You do not have permission to perform this action"):
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=detail
        )
        