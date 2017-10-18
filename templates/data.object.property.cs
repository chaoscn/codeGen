        protected $dataObjectDataType _$dataObjectPropertyInLowerCase;
        [$dataObjectXmlSerialize]
        public virtual $dataObjectDataType $dataObjectPropertyInUpperCase
        {
            get { return _$dataObjectPropertyInLowerCase; }
            set
            {
                if (!object.Equals(_$dataObjectPropertyInLowerCase, value))
                {
                    IsDirty = true;
                    _$dataObjectPropertyInLowerCase = value;
                }
            }
        }

