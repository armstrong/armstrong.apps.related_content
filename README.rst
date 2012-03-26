armstrong.apps.related_content
==============================
Provides mechanism for relating content to other models

You can use ``armstrong.apps.related_content`` to link two separate models
together through a ``GenericForeignKey`` for the ``source`` and the
``destination``.  You can further organize the relationship with
``RelatedType`` (think: "articles", "images", "external_links", and so on) and
all relationships are ordered.


Usage
-----
You do *not* have to change your models to utilize related content---it exists
outside of your model.  There are two fields that you can add that give you
easy access to your related content:

* ``armstrong.apps.related_content.fields.RelatedObjectsField``
* ``armstrong.apps.related_content.fields.ReverseRelatedObjectsField``

The first let's you access objects where your model is the ``source``, the
latter lets you access objects where your model is the ``destination``.  Note
that these return the *actual* models that are related, not the
``RelatedContent`` model.  If you need access to the raw ``RelatedContent``
model directly from your model, see
``armstrong.apps.related_content.fields.RelatedContentField``.

You can also use the ``RelatedContentInline`` for exposing an admin interface
to your related content inside Django's admin.


Accessing Related Content
"""""""""""""""""""""""""
You can access fields through the ``RelatedObjectsField`` or
``ReverseRelatedObjectsField`` by calling ``all()`` or
``by_type("some_type")``.  These return QuerySet-like objects, but since they
are generic relationships, they're not quite QuerySets.

Inside templates, you can access related content by type using the dot-syntax.
For example, you could load the first related content of a type ``"articles"``
with this syntax:

::

    {{ my_article.related.articles.0 }}


Installation & Configuration
----------------------------
You can install the latest release of ``armstrong.apps.related_content`` using
`pip`_:

::

    pip install armstrong.apps.related_content

Make sure to add ``armstrong.apps.related_content`` to your ``INSTALLED_APPS``.
You can add this however you like.  This works as a copy-and-paste solution:

::

	INSTALLED_APPS += ["armstrong.apps.related_content", ]

Once installed, you have to run either ``syncdb``, or ``migrate`` if you are
using `South`_.

.. _pip: http://www.pip-installer.org/
.. _South: http://south.aeracode.org/


Contributing
------------

* Create something awesome -- make the code better, add some functionality,
  whatever (this is the hardest part).
* `Fork it`_
* Create a topic branch to house your changes
* Get all of your commits in the new topic branch
* Submit a `pull request`_

.. _pull request: http://help.github.com/pull-requests/
.. _Fork it: http://help.github.com/forking/


State of Project
----------------
Armstrong is an open-source news platform that is freely available to any
organization.  It is the result of a collaboration between the `Texas Tribune`_
and `Bay Citizen`_, and a grant from the `John S. and James L. Knight
Foundation`_.

To follow development, be sure to join the `Google Group`_.

``armstrong.apps.related_content`` is part of the `Armstrong`_ project.  You're
probably looking for that.

.. _Texas Tribune: http://www.texastribune.org/
.. _Bay Citizen: http://www.baycitizen.org/
.. _John S. and James L. Knight Foundation: http://www.knightfoundation.org/
.. _Google Group: http://groups.google.com/group/armstrongcms
.. _Armstrong: http://www.armstrongcms.org/


License
-------
Copyright 2011-2012 Bay Citizen and Texas Tribune

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
