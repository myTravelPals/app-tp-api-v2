from django.db import IntegrityError
from ninja import Router
from .models import ClientRegistration, ContactUsMessage
from .schemas import ClientRegistrationSchema, CreateClientRegistrationSchema, CreateContactUsMessageSchema, \
    ContactUsMessageSchema, ErrorResponseSchema

router = Router()


@router.post("/client_registration",
             response={201: ClientRegistrationSchema,
                       400: ErrorResponseSchema,
                       405: ErrorResponseSchema,
                       409: ErrorResponseSchema})
def create_client_registration(request, data: CreateClientRegistrationSchema):
    try:
        # Attempt to create the client registration
        client_registration = ClientRegistration.objects.create(**data.model_dump())
        print(client_registration.id)
        print(client_registration.email)
        print(client_registration.date_registered)
        print(f"Client registration created!")
        # Successful creation
        return 201, {"message": "Client Registered successfully!", "email": client_registration.email}

    except IntegrityError as e:
        # Conflict: Likely a duplicate entry
        print(str(e))
        return 409, {"message": "Client email already exists."}

    except ValueError as e:
        # Bad request: Data validation issues
        print(str(e))
        return 400, {"message": str(e)}

    except Exception as e:
        # Generic error or unhandled cases
        print(str(e))
        return 400, {"message": "An unexpected error occurred: " + str(e)}


@router.post("/contact_us_message", response=ContactUsMessageSchema)
def create_contact_us_message(request, data: CreateContactUsMessageSchema):
    contact_us_message = ContactUsMessage.objects.create(**data.model_dump())
    return contact_us_message