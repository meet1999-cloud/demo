ef add_column(engine, table_name, column):
    column_name = column.compile(dialect=engine.dialect)
    column_type = column.type.compile(engine.dialect)
    engine.execute('ALTER TABLE %s ADD COLUMN %s %s' % (table_name, column_name, column_type))


column = Column('firstname', String(50), primary_key=True)
column1 = Column('lastname', String(50))
column2 = Column('PhoneNumber', Numeric(10))
column3 = Column('Email', String(50))
column4 = Column('DOB', (Date()))

add_column(engine=engine, table_name='person', column=column1)
add_column(engine=engine, table_name='person', column=column2)
add_column(engine=engine, table_name='person', column=column3)
add_column(engine=engine, table_name='person', column=column4)
