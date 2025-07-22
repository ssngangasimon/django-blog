# Django Blog

<pre> ```mermaid classDiagram class Category { +id +name } class Tag { +id +name } class Post { +id +title +content +author +created_at +category } Category <|-- Post : belongs to Post --> Tag : many-to-many ``` </pre>