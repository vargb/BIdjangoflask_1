from flask import Flask, request, jsonify, logging
from flask_migrate import Migrate
from database import db, graphql
import csv
from io import TextIOWrapper,StringIO
from ariadne import load_schema_from_path, make_executable_schema, \
    graphql_sync, QueryType,MutationType, gql,exceptions, explorer
from graphql import GraphQLError


def server(srv:Flask)->Flask:
    db.postgredb.init_app(srv)
    with srv.app_context():
        loggy=logging.create_logger(srv)
    
    migrate=Migrate(srv,db.postgredb)
    
    @srv.route("/uploadCSV",methods=["POST"])
    def csvParser():
        file=request.files['BiCsv']
        if not file or file.filename=='':
            return jsonify({"HeadsUp":"Cant get no file here"}),400
        
        if file:
            stream=TextIOWrapper(file.stream,encoding='utf-8')
            csv_reader=csv.reader(stream)
            next(csv_reader)
            for row in csv_reader:
                data=db.BiModel(product_id=row[0],category=row[1],industry=row[2],business_scale=row[3],user_type=row[4],no_of_users=row[5],deployment=row[6],os=row[7],mobile_apps=row[8],pricing=row[9],rating=row[10],id=db.encrypt_string(row[0]))
                db.postgredb.session.add(data)
            loggy.info("uploading to DB...")
            db.postgredb.session.commit()
            return jsonify({"HeadsUp":"CSV imported to database"}),200
    
    
    schema = getGraphqlSchema("C:\VGBPython\graphql-flask\\flask2\\flaskServer2\\flaskServer\schema.graphql")
    if schema is None:
        return GraphQLError("error in getting schema")
    
    @srv.route("/graphql",methods=["GET"])
    def graphql_playground():
        return explorer.ExplorerGraphiQL().html(None),200
    
    @srv.route("/graphql", methods=["POST"])
    def graphql_server():
        data=request.get_json()
        success, result = graphql_sync(
            schema,
            data,
            context_value=request,
            debug=srv.debug
        )
        status_code = 200 if success else 400
        return jsonify(result), status_code
    
    
    return srv

def getGraphqlSchema(schemaPath:str):
    try:
        type_defs=gql(load_schema_from_path(schemaPath))
    except exceptions.GraphQLFileSyntaxError:
        return None
    query=QueryType()
    mutation=MutationType()
    
    mutation.set_field("Upload", graphql.resolve_Upload)
    mutation.set_field("deletebyID",graphql.resolve_deletebyID)
    
    query.set_field("getbyID",graphql.resolve_getbyID)
    query.set_field("getbyCategory",graphql.resolve_getbyCategory)
    
    return make_executable_schema(type_defs,query,mutation)