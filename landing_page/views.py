from ninja import Router
from .models import ClientRegistration, ContactUsMessage
from .schemas import ClientRegistrationSchema, CreateClientRegistrationSchema, CreateContactUsMessageSchema, \
    ContactUsMessageSchema

router = Router()


@router.post("/client_registration", response=ClientRegistrationSchema)
def create_client_registration(request, data:CreateClientRegistrationSchema):
    client_registration = ClientRegistration.objects.create(**data.model_dump())
    return client_registration

@router.post("/contact_us_message", response=ContactUsMessageSchema)
def create_contact_us_message(request, data:CreateContactUsMessageSchema):
    contact_us_message = ContactUsMessage.objects.create(**data.model_dump())
    return contact_us_message

