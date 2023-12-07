from .db import BiModel,encrypt_string,postgredb
from graphql import GraphQLError


# Query Resolver
def resolve_getbyID(_, info, product_Id):
    try:
        data = BiModel.query.filter_by(product_id=product_Id).first()
        if not data:
            raise GraphQLError("No data found for the provided ID")
        return {
            "product_Id": data.product_id,
            "industry": data.industry,
            "category": data.category,
            "business_scale":data.business_scale,
            "user_type":data.user_type,
            "no_of_users":data.no_of_users,
            "deployment":data.deployment,
            "os":data.os,
            "mobile_apps":data.mobile_apps,
            "pricing":data.pricing,
            "rating":data.rating,
            "id":data.id
        }
    except Exception as e:
        raise GraphQLError(f"Error - {str(e)}")

def resolve_getbyCategory(_, info, category):
    try:
        data = BiModel.query.filter_by(category=category).all()
        if not data:
            return [GraphQLError("No data found for the provided category")]
        return [
            {
                "product_Id": dat.product_id,
                "industry": dat.industry,
                "category": dat.category,
                "business_scale":dat.business_scale,
                "user_type":dat.user_type,
                "no_of_users":dat.no_of_users,
                "deployment":dat.deployment,
                "os":dat.os,
                "mobile_apps":dat.mobile_apps,
                "pricing":dat.pricing,
                "rating":dat.rating,
                "id":dat.id
            } for dat in data
        ]
    except Exception as e:
        raise GraphQLError(f"Error - {str(e)}")

# Mutation Resolver
def resolve_Upload(_, info, product_Id,category,industry,business_scale,user_type,no_of_users,deployment,os,mobile_apps,pricing,rating):
    try:
        data = BiModel.query.filter_by(product_id=product_Id).first()
        
        if data is None:
            new_entry = BiModel(
                product_id=product_Id,
                category=category,
                industry=industry,
                business_scale=business_scale,
                user_type=user_type,
                no_of_users=no_of_users,
                deployment=deployment,
                os=os,
                mobile_apps=mobile_apps,
                pricing=pricing,
                rating=rating,
                id=encrypt_string(str(product_Id))
            )
            postgredb.session.add(new_entry)
            postgredb.session.commit()
            return {
                "product_Id": new_entry.product_id,
                "industry": new_entry.industry,
                "category": new_entry.category,
                "business_scale":new_entry.business_scale,
                "user_type":new_entry.user_type,
                "no_of_users":new_entry.no_of_users,
                "deployment":new_entry.deployment,
                "os":new_entry.os,
                "mobile_apps":new_entry.mobile_apps,
                "pricing":new_entry.pricing,
                "rating":new_entry.rating,
                "id":new_entry.id
            }
        else:
            return GraphQLError("Product ID already present!")
    except Exception as e:
        raise GraphQLError(f"Error in uploading - {str(e)}")
