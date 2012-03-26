armstrong.apps.related_content
==============================
Provides mechanism for relating content to other models

Overview
--------

armstrong.apps.related_content provides a model that generically links objects
as well as providing a type and ordering for those links. The heart of the system is
the RelatedContent type which consits of a GenericForeignKey to a source object, a
GenericForeignKey to a destination object, an IntegerField for order and a ForeignKey
to a RelatedType object that consists of a title.


Creating RelatedContent objects
-------------------------------

This package provides ``armstrong.apps.related_content.admin.RelatedContentInline`` which
should be the primary way that staff interact with the related_content system.

For python access, we provide ``armstrong.apps.related_content.fields.RelatedContentField``
which is a `GenericRelation`_ that has the right defaults to work with the related_content
system.

.. _GenericRelation: https://docs.djangoproject.com/en/dev/ref/contrib/contenttypes/#reverse-generic-relations


Accessing Related Content
-------------------------

For convenient access, we provide ``armstrong.apps.related_content.fields.RelatedObjectsField``
and ``armstrong.apps.related_content.fields.ReverseRelatedObjectsField``. These fields
utilize the GenericForeignKeyQuerySet for efficient access of the objects on the
far side of the RelatedContent objects. For example::

		obj.related['lead_art'][0] 
		# retrieves the destination_object from the first RelatedContent object with
		# a RelatedType with title 'lead_art'

While this syntax might seem somewhat strange, it allows for convenient usage in templates::

		{% load layout_helpers %}
		{% render_model object.related.lead_art.0 'lead_art' %}

This usage will render the lead_art.html template that is appropriate for the type that
the user has associated with the object. This means you can have a lead_art relationship
to an Image, or an ImageSet or an embeded video type as long as you have a lead_art.html
template in the right place.


Installation
------------

::

    name="armstrong.apps.related_content"
    pip install -e git://github.com/armstrong/$name#egg=$name


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
