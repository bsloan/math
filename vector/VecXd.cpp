//
//  VecXd.cpp
//
//  Created by Brian Sloan on 2/1/14.
//

#include <stdexcept>
#include "VecXd.h"

// Constructor
template <class T>
VecXd<T>::VecXd()
{
  this->D = 0;
  this->contents = nullptr;
}

// Copy constructor
template <class T>
VecXd<T>::VecXd(const VecXd<T> &rhs)
{
  this->D = rhs.D;
  this->contents = new T[D];
  for (int i = 0; i < this->D; ++i)
  {
    this->contents[i] = rhs.contents[i];
  }
}

// Move constructor
template <class T>
VecXd<T>::VecXd(const VecXd<T> &&rhs)
{
  this->contents = rhs.contents;
  rhs.contents = nullptr;
}

// Copy assignment constructor
template <class T>
VecXd<T> &VecXd<T>::operator=(const VecXd<T> &rhs)
{
  if (this != &rhs)
  {
    this->VecXd::~VecXd(); // deallocate any memory used by lhs
    this->D = rhs.D;
    this->contents = new T[D];
    for (int i = 0; i < rhs.D; ++i)
    {
      this->contents[i] = rhs.contents[i];
    }
    return *this;
  }
  else
  {
    return *this;
  }
}

// Move assignment constructor
template <class T>
VecXd<T> &VecXd<T>::operator=(const VecXd<T> &&rhs)
{
  std::swap(D, rhs.D);
  std::swap(this->contents, rhs.contents);
  return *this;
}

// Addition operator: +=
template <class T>
VecXd<T> &VecXd<T>::operator+=(const VecXd<T> &rhs)
{
  if (this->D != rhs.D)
  {
    throw std::invalid_argument("cannot add vectors of different sizes");
  }
  
  for (int i = 0; i < this->D; ++i)
  {
    this->contents[i] += rhs.contents[i];
  }
  return *this;
}

// Addition operator: +
template <class T>
VecXd<T> &operator+(VecXd<T> lhs, const VecXd<T> &rhs)
{
  return lhs += rhs;
}

// Output stream operator
template <typename U>
ostream &operator<<(ostream &out, VecXd<U> &vec)
{
  for (int i = 0; i < vec.D; ++i)
  {
    out << vec.contents[i] << " ";
  }
  return out;
}

// Input stream operator
template <typename U>
istream &operator>>(istream &in, VecXd<U> &vec)
{
  if (vec.D < 1)
  { // vector is not initialized; read size from input and allocate
    in >> vec.D;
    if (!std::cin.good())
    {
      throw std::invalid_argument("type mismatch on input");
    }
    vec.contents = new U[vec.D];
    for (int i = 0; i < vec.D; ++i)
    {
      in >> vec.contents[i];
      if (!std::cin.good())
      {
        throw std::invalid_argument("type mismatch on input");
      }
    }
  }
  else
  { // vector already initialized; read D items from input
    for (int i = 0; i < vec.D; ++i)
    {
      in >> vec.contents[i];
    }
  }
  return in;
}

// Destructor
template <class T>
VecXd<T>::~VecXd()
{
  if (this->D > 0) delete[] contents;
}
